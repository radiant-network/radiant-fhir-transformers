import logging
import uuid
from abc import ABC, abstractmethod
from typing import Any

from .transformer_config import TransformConfig

logger = logging.getLogger(__name__)


def walk_dict_path(data: dict, path: str):
    """Walk down a FHIR-style path like 'low.value' in a nested dict."""
    current = data
    for part in path.split("."):
        if isinstance(current, list):
            current = [
                item.get(part) for item in current if isinstance(item, dict)
            ]
        elif isinstance(current, dict):
            current = current.get(part)
        else:
            return None
    return current


def extract_from_dict(item, mapping: TransformConfig):
    return {
        col: walk_dict_path(item, column_config.fhir_key)
        for col, column_config in mapping.columns.items()
    }


def extract_from_primitive(item, mapping: TransformConfig):
    if len(mapping.columns) != 1:
        raise ValueError("Primitive values require single-column mapping")
    return {next(iter(mapping.columns)): item}


def extract_from_str(item: str, mapping: TransformConfig):
    if len(mapping.columns) != 1:
        raise ValueError("Primitive values require single-column mapping")
    return {next(iter(mapping.columns)): item}


def extract_fhir_reference_prefix(fhir_raw_value: str) -> str:
    return fhir_raw_value.rsplit("/", 1)[-1]


EXTRACTION_STRATEGIES = {
    dict: extract_from_dict,
    str: extract_from_str,
    int: extract_from_primitive,
    float: extract_from_primitive,
    bool: extract_from_primitive,
}


class ResultHandler(ABC):
    """Abstract base class for handling different types of FHIRPath results."""

    @abstractmethod
    def handle(
        self, raw_result: Any, config: TransformConfig
    ) -> list[dict[str, Any]]:
        """Transform raw FHIRPath result into output rows."""
        pass


class SingleResultHandler(ResultHandler):
    """Handles single-value FHIRPath results."""

    def handle(
        self, raw_result: Any, config: TransformConfig
    ) -> list[dict[str, Any]]:
        """Transform a single result into one output row."""
        if isinstance(raw_result, (dict, str, int, float, bool)):
            return [self._extract_values(raw_result, config)]
        logger.warning("Unexpected single result type: %s", type(raw_result))
        return [self._create_null_row(config)]

    def _extract_values(
        self, item: Any, config: TransformConfig
    ) -> dict[str, Any]:
        """Extract values from a single result item."""
        strategy = EXTRACTION_STRATEGIES.get(type(item))
        if not strategy:
            logger.warning("Unable to extract values from single result")
            return self._create_null_row(config)
        values = strategy(item, config)
        if config.fhir_reference:
            values[config.fhir_reference] = extract_fhir_reference_prefix(
                values[config.fhir_reference]
            )
        return values

    def _extract_reference_id(self, reference: Any) -> str:
        """Extract ID from FHIR reference string."""
        if not isinstance(reference, str):
            logger.warning(
                "FHIR reference must be a string, got %s", type(reference)
            )
            return reference
        return reference.rsplit("/", 1)[-1]

    def _create_null_row(self, config: TransformConfig) -> dict[str, Any]:
        """Create a row with null values for all columns."""
        return {col_name: None for col_name in config.columns}


class ListResultHandler(ResultHandler):
    """Handles list-type FHIRPath results."""

    def __init__(self):
        self.single_handler = SingleResultHandler()

    def handle(
        self, raw_result: Any, config: TransformConfig
    ) -> list[dict[str, Any]]:
        """Transform a list result into multiple output rows."""
        if not isinstance(raw_result, list):
            logger.warning("Expected list result, got %s", type(raw_result))
            return [self.single_handler._create_null_row(config)]

        return [
            self.single_handler._extract_values(item, config)
            for item in raw_result
        ]


class IDGeneratorHandler(ResultHandler):
    """Handles ID generation for resource subtypes."""

    def handle(
        self, raw_result: Any, config: TransformConfig
    ) -> list[dict[str, Any]]:
        """Generate a UUID for the ID column."""
        if "id" not in config.columns:
            logger.warning("ID column not in config for ID generation")
            return [{}]
        return [{"id": str(uuid.uuid4())}]


class NoOpHandler(ResultHandler):
    """Handles No Operation generation for resource subtypes."""

    def handle(
        self, raw_result: Any, config: TransformConfig
    ) -> list[dict[str, Any]]:
        return [{col: None for col in config.columns.keys()}]


class ResultHandlerFactory:
    """Factory for creating appropriate result handlers."""

    @staticmethod
    def get_handler(
        raw_result: Any, config: TransformConfig, is_subtype: bool = False
    ) -> ResultHandler:
        """Determine and return the appropriate result handler."""
        if is_subtype and config.fhir_path is None and "id" in config.columns:
            return IDGeneratorHandler()

        if not raw_result:
            return NoOpHandler()

        if isinstance(raw_result, list):
            return ListResultHandler()

        return SingleResultHandler()
