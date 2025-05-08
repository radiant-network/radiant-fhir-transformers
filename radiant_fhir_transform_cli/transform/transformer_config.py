from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from .exceptions import InvalidTransformConfigError


class DataType(str, Enum):
    """Supported data types for transformation output."""

    INTEGER = "int"
    STRING = "str"
    BOOLEAN = "bool"
    DATETIME = "datetime"


@dataclass
class ColumnConfig:
    """Configuration for a single output column."""

    fhir_key: str
    type: DataType


@dataclass
class TransformConfig:
    """Configuration for a FHIR path transformation."""

    fhir_path: str
    columns: dict[str, ColumnConfig]
    is_foreign_key: bool
    fhir_reference: Optional[str] = None


def extract_raw_transform_schema(
    transform_schema: list[dict[str, str | dict]],
) -> list[TransformConfig]:
    configs = []
    for entry in transform_schema:
        fhir_path = entry.get("fhir_path")
        fhir_reference = entry.get("fhir_reference")
        raw_columns = entry.get("columns", {})
        is_foreign_key = entry.get("is_foreign_key", False)
        columns = {
            col_name: ColumnConfig(
                fhir_key=col_cfg.get("fhir_key"), type=DataType(col_cfg["type"])
            )
            for col_name, col_cfg in raw_columns.items()
        }
        config = TransformConfig(
            fhir_path=fhir_path,
            columns=columns,
            fhir_reference=fhir_reference,
            is_foreign_key=is_foreign_key,
        )
        configs.append(config)

    return configs


@dataclass
class TransformationSchema:
    """Container for all transformation configurations for a FHIR resource type."""

    configs: list[TransformConfig] = field(default_factory=list)
    resource_type: str = ""
    resource_subtype: Optional[str] = None

    def __init__(self, transform_schema: list[dict[str, str | dict]]):
        self.configs = extract_raw_transform_schema(transform_schema)

    def __post_init__(self):
        self._validate()

    def _validate(self):
        """Validate the complete transformation schema."""
        if not self.configs:
            raise InvalidTransformConfigError(
                f"Empty transform configuration for {self.resource_type}"
            )

        foreign_key: Optional[str] = None
        seen_paths = set()
        for config in self.configs:
            if config.is_foreign_key:
                if foreign_key:
                    raise InvalidTransformConfigError(
                        f"Duplicate Foreign Key Set: {config.fhir_path}"
                    )
                if len(config.columns) > 1:
                    raise InvalidTransformConfigError(
                        f"Foreign Key can only be set to one column:  {config.fhir_path}"
                    )
                foreign_key = next(iter(config.columns))

            if config.fhir_path in seen_paths:
                raise InvalidTransformConfigError(
                    f"Duplicate FHIR path: {config.fhir_path}"
                )
            seen_paths.add(config.fhir_path)
        if self.resource_subtype and not foreign_key:
            raise InvalidTransformConfigError(
                f"Foreign Key must be set for subtype {self.resource_subtype}"
            )

    def get_config_by_path(self, path: str) -> Optional[TransformConfig]:
        """Get a config by its FHIR path."""
        return next((c for c in self.configs if c.fhir_path == path), None)

    @property
    def foreign_key(self) -> Optional[str]:
        foreign_key: Optional[str] = None
        for config in self.configs:
            if config.is_foreign_key:
                foreign_key = next(iter(config.columns))
                break

        return foreign_key

    @property
    def all_column_names(self) -> list[str]:
        """Get all output column names across all configs."""
        columns = []
        for config in self.configs:
            columns.extend(config.columns.keys())
        return columns
