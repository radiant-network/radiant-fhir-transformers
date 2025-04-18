"""
FHIR transformers

This transformation dictionary defines how to extract and map fields from FHIR
resource JSON objects into a flat dictionary format suitable for CSV output
or other tabular representations.

Transform Dictionary
--------------------
Structure:
- Each item in the list corresponds to a specific field in the FHIR Observation
resource.
- 'fhir_path': A string representing the path to the desired field within the
FHIR resource.
- 'columns': A dictionary mapping output CSV column names to their corresponding
extraction details:
    - 'fhir_key': The key used to extract the value from the FHIR resource.
    - 'type': The expected data type of the extracted value (e.g., 'str', 'int').

Example Entry:
{
    "fhir_path": "id",
    "columns": {
        "id": {
            "fhir_key": "id",
            "type": "str"
        }
    }
}
Usage:
This dictionary is utilized by the `FhirResourceTransformer` base class and its
subclasses to systematically extract and transform data from FHIR resources into
a flat structure. Subclasses must create their own dictionary to
accommodate resource-specific fields and transformation logic.
"""

import json
import logging
from dataclasses import dataclass, field
from pprint import pformat
from typing import Any, Generator, Iterable, Optional

import pandas
from fhirpathpy import evaluate

from .exceptions import FhirTransformError
from .result_handler import ResultHandlerFactory
from .transformer_config import TransformationSchema

logger = logging.getLogger(__name__)


class DataType:
    INTEGER = "int"
    STRING = "str"
    BOOLEAN = "bool"
    DATETIME = "datetime"


def _validate_transform_dict(cls_name, transform_dict):
    """
    Check that column map has correct types and is not empty
    """
    msg = (
        f"❌ Invalid column map in {cls_name}. "
        "Keys must be must be strings representing column names in the "
        "output csv and values must be valid FHIR path expressions"
    )

    if not transform_dict:
        raise ValueError(msg)

    for transform_config in transform_dict:
        fhir_path = transform_config.get("fhir_path")
        columns = transform_config.get("columns")

        if not isinstance(columns, dict):
            raise ValueError(msg)


@dataclass
class FhirTransformationResultBuilder:
    base_attributes: dict[str, Any] = field(default_factory=dict)
    list_member_rows: list[dict[str, Any]] = field(default_factory=list)

    def add_base_attributes(self, values: dict[str, Any]) -> None:
        self.base_attributes.update(values)

    def add_list_member_rows(self, rows: list[dict[str, Any]]) -> None:
        if self.list_member_rows:
            raise FhirTransformError(
                "Cannot add multiple list member expansions"
            )
        self.list_member_rows = rows

    def build_result(self) -> list[dict[str, Any]]:
        if not self.list_member_rows:
            return [self.base_attributes]
        return [
            {**self.base_attributes, **row} for row in self.list_member_rows
        ]


class FhirResourceTransformer:
    """
    Abstract base class to transform FHIR resources into a column dictionary

    Extracts values from FHIR resources using FHIRPath expressions defined
    in the transform_dict.

    Transform dict
    --------------
    Keys are output columns in a csv file. Values are FHIR path expressions to
    the field value to be extracted from the FHIR JSON object

    See https://hl7.org/fhir/R4/fhirpath.html for FHIRPath spec

    Attributes:
        resource_type (str): The type of the FHIR resource (e.g., 'Patient').
        transform_dict (dict): A mapping of output columns to FHIRPath
          expressions
    """

    def __init__(
        self,
        resource_type: str,
        resource_subtype: Optional[str],
        transform_dict: list[dict[str, str | dict]],
    ):
        """
        Initializes the transformer with the resource type and column map.

        Args:
            resource_type (str): The type of the FHIR resource.
            transform_dict (dict): FHIRPath-to-column name mapping.
        """
        self.resource_type = resource_type
        self.resource_subtype = resource_subtype

        # Validate transforms
        _validate_transform_dict(type(self).__name__, transform_dict)
        self.transform_dict = transform_dict

    def transform_resource(
        self, resource_idx: int, resource_dict: dict
    ) -> list[dict]:
        """
        Transforms the given FHIR resource dictionary based on the column map.

        Evaluates each FHIRPath expression and returns a dictionary with the
        corresponding column names as keys and evaluated values as values.

        Args:
            resource_dict (dict): A dictionary representing a FHIR resource.

        Returns:
            dict: A dictionary with column names and evaluated FHIRPath values.
        """
        transform_result_builder = FhirTransformationResultBuilder()
        transformation_schema = TransformationSchema(self.transform_dict)
        for config in transformation_schema.configs:
            fhir_path_expression = config.fhir_path

            raw_items = (
                evaluate(resource_dict, fhir_path_expression)
                if fhir_path_expression
                else None
            )
            fhir_path_output_handler = ResultHandlerFactory.get_handler(
                raw_items, config, is_subtype=self.resource_subtype is not None
            )

            result = fhir_path_output_handler.handle(raw_items, config)
            if len(result) == 1:
                transform_result_builder.add_base_attributes(result[0])
            else:
                transform_result_builder.add_list_member_rows(result)

        final_results = transform_result_builder.build_result()
        logger.debug(
            "Transformed %s %s into %s",
            self.resource_type,
            resource_idx,
            pformat(final_results),
        )

        return final_results

    def transform_from_ndjson(
        self, ndjson_filepath: str
    ) -> Generator[list[dict], None, None]:
        """
        Transforms data from an NDJSON file into a list of dictionaries.

        Args:
            ndjson_filepath (str): The path to the NDJSON file to transform.

        Yields:
            dict: A dictionary representing each record in the NDJSON file.

        Returns:
            Generator[dict, None, list[dict]]: A generator that yields
              dictionaries for each record and returns a list of all
              dictionaries at the end.
        """
        with open(ndjson_filepath, "r") as f:
            for i, line in enumerate(f):
                yield self.transform_resource(i, json.loads(line.strip()))

    def transform_from_json(
        self, json_filepath
    ) -> Generator[list[dict], None, None]:
        """
        Transforms data from a JSON file into a list of dictionaries.

        Args:
            json_filepath (str): The path to the JSON file to transform.

        Yields:
            dict: A dictionary representing each record in the JSON file.

        Returns:
            Generator[dict, None, list[dict]]: A generator that yields
              dictionaries for each record and returns a list of all
              dictionaries at the end.
        """
        with open(json_filepath, "r") as f:
            data = json.load(f)
            if isinstance(data, dict):
                objs = [data]
            else:
                objs = data

            for i, resource in enumerate(objs):
                yield self.transform_resource(i, resource)

    def write_to_csv(self, row_dicts: Iterable[dict], csv_filepath):
        """
        Writes a list of dictionaries to a CSV file.

        Args:
            row_dicts (Iterable[dict]): An iterable of dictionaries to write
              to the CSV file.
            csv_filepath (str): The path where the CSV file will be written.

        Returns:
            None
        """
        return pandas.DataFrame([r for r in row_dicts]).to_csv(
            csv_filepath, index=False
        )
