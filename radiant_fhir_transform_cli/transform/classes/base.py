"""
FHIR Resource Transformer Module
================================

This module defines a base class for transforming FHIR resources into tabular
representations (e.g., CSV, DataFrame) using **SQL-on-FHIR** evaluation logic.

Overview
--------
Instead of manually evaluating FHIRPath expressions, this implementation
leverages the `sqlonfhir` library to evaluate FHIR `ViewDefinition` resources.
Each `ViewDefinition` specifies which fields to extract and how to structure
the flattened output from nested FHIR resources.

The transformer is designed to:
- Read FHIR resource JSON or NDJSON files.
- Evaluate them using a SQL-on-FHIR `ViewDefinition`.
- Convert the results into a list of dictionaries suitable for CSV export
  or further analysis.
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

        This class provides functionality for evaluating FHIR resources using
    `sqlonfhir.evaluate()` based on a provided `ViewDefinition`. The evaluated
    output is then transformed into a flat list of dictionaries suitable for
    writing to CSV or other tabular formats.

    Attributes:
        resource_type (str): The FHIR resource type (e.g., 'Patient', 'Observation').
        resource_subtype (str | None): Optional subtype (e.g., 'Component').
        table_name (str): Generated name for the output table or CSV.
        view_definition (dict): The SQL-on-FHIR `ViewDefinition` used for transformation.
    """

    def __init__(
        self,
        resource_type: str,
        resource_subtype: str | None,
        view_definition: dict,
    ):
        """
        Initialize a FHIR resource transformer.

        Args:
            resource_type (str): The FHIR resource type to transform.
            resource_subtype (str | None): Optional subtype for more granular naming.
            view_definition (dict): SQL-on-FHIR ViewDefinition used to define extraction logic.
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
        Apply the ViewDefinition to a single FHIR resource.

        Args:
            resource_idx (int): Index of the resource (used for logging).
            resource_dict (dict): A FHIR resource JSON object.

        Returns:
            list[dict[str, str]]: Flattened tabular results produced by `sqlonfhir.evaluate()`.
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
