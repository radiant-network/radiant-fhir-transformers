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
from collections.abc import Generator, Iterable
from pprint import pformat
from typing import Any

import pandas
from sqlonfhir import evaluate

from radiant_fhir_transform_cli.utils.misc import camel_to_snake

logger = logging.getLogger(__name__)


def generate_table_name(
    resource_type: str, resource_subtype: str | None
) -> str:
    table_name = camel_to_snake(resource_type)
    if resource_subtype:
        table_name = f"{table_name}_{camel_to_snake(resource_subtype)}"
    return table_name


class FhirResourceTransformer:
    """
    Abstract base class to transform FHIR resources into a column dictionary

    Extracts values from FHIR resources using FHIRPath expressions defined
    in the transform_dict.

    Transform schema
    --------------
    Keys are output columns in a csv file. Values are FHIR path expressions to
    the field value to be extracted from the FHIR JSON object

    See https://hl7.org/fhir/R4/fhirpath.html for FHIRPath spec

    Attributes:
        resource_type (str): The type of the FHIR resource (e.g., 'Patient').
        transform_schema (list[dict]): A mapping of output columns to FHIRPath
          expressions
    """

    def __init__(
        self,
        resource_type: str,
        resource_subtype: str | None,
        view_definition: dict,
    ):
        """
        Initializes the transformer with the resource type and column map.

        Args:
            resource_type (str): The type of the FHIR resource.
            transform_dict (dict): FHIRPath-to-column name mapping.
        """
        self.resource_type: str = resource_type
        self.resource_subtype: str | None = resource_subtype
        self.table_name: str = generate_table_name(
            resource_type, resource_subtype
        )
        self.view_definition: dict = view_definition

    def transform_resource(
        self, resource_idx: int, resource_dict: dict
    ) -> list[dict[str, str]]:
        """
        Transforms the given FHIR resource dictionary based on the column map.

        Evaluates each FHIRPath expression and returns a dictionary with the
        corresponding column names as keys and evaluated values as values.

        Args:
            resource_dict (dict): A dictionary representing a FHIR resource.

        Returns:
            dict: A dictionary with column names and evaluated FHIRPath values.
        """
        results = evaluate(
            resources=[resource_dict], view_definition=self.view_definition
        )

        logger.debug(
            "Transformed %s %s into %s",
            self.resource_type,
            resource_idx,
            pformat(results),
        )

        return results

    def transform_from_ndjson(
        self, ndjson_filepath: str
    ) -> Generator[list[dict[str, Any]], None, None]:
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
    ) -> Generator[list[dict[str, Any]], None, None]:
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

    def write_to_csv(
        self, row_dicts: Iterable[dict[str, Any]], csv_filepath: str
    ):
        """
        Writes a list of dictionaries to a CSV file.

        Args:
            row_dicts (Iterable[dict]): An iterable of dictionaries to write
              to the CSV file.
            csv_filepath (str): The path where the CSV file will be written.

        Returns:
            None
        """
        first_batch = True
        for row_dict in row_dicts:
            df = pandas.DataFrame(row_dict)
            df.to_csv(
                csv_filepath,
                mode="w" if first_batch else "a",
                header=first_batch,
                index=False,
            )
            first_batch = False
