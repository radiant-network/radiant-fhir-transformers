import json
import logging
from typing import Generator, Iterable
from pprint import pformat

import pandas
from fhirpathpy import evaluate

logger = logging.getLogger(__name__)


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

    for key, value in transform_dict.items():
        if not isinstance(key, str) or not isinstance(value, str):
            raise ValueError(msg)


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
        transform_dict: dict[str, str],
    ):
        """
        Initializes the transformer with the resource type and column map.

        Args:
            resource_type (str): The type of the FHIR resource.
            transform_dict (dict): FHIRPath-to-column name mapping.
        """
        self.resource_type = resource_type

        # Validate transforms
        _validate_transform_dict(type(self).__name__, transform_dict)
        self.transform_dict = transform_dict

    def transform_resource(
        self, resource_idx: int, resource_dict: dict
    ) -> dict:
        """
        Transforms the given FHIR resource dictionary based on the column map.

        Evaluates each FHIRPath expression and returns a dictionary with the
        corresponding column names as keys and evaluated values as values.

        Args:
            resource_dict (dict): A dictionary representing a FHIR resource.

        Returns:
            dict: A dictionary with column names and evaluated FHIRPath values.
        """
        result = {}
        for col_name, fhir_path_expression in self.transform_dict.items():
            values = evaluate(resource_dict, fhir_path_expression)
            print(values)

            if isinstance(values, list):
                if len(values) > 0:
                    value = values[0]
                else:
                    value = None
            else:
                value = values

            result[col_name] = value

        logger.info(
            "Transformed %s %s into %s",
            self.resource_type, resource_idx, pformat(result)
        )
        return result

    def transform_from_ndjson(
        self, ndjson_filepath: str
    ) -> Generator[dict, None, list[dict]]:
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
        with open(ndjson_filepath, 'r') as f:
            for i, line in enumerate(f):
                yield self.transform_resource(i, json.loads(line.strip()))

    def transform_from_json(
        self, json_filepath
    ) -> Generator[dict, None, list[dict]]:
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
        with open(json_filepath, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                objs = [data]
            else:
                objs = data

            for i, resource in enumerate(objs):
                self.transform_resource(i, resource)

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
        return pandas.DataFrame(
            [r for r in row_dicts]
        ).to_csv(csv_filepath, index=False)
