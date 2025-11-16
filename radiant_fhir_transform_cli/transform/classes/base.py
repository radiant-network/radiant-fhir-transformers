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
  • Read FHIR resource JSON or NDJSON files.
  • Evaluate them using a SQL-on-FHIR `ViewDefinition`.
  • Convert the results into a list of dictionaries suitable for CSV export
    or further analysis.
"""

import csv
import json
import logging
import uuid
from collections.abc import Generator, Iterable
from pprint import pformat
from typing import Any

from sqlonfhir import evaluate
from radiant_fhir_transform_cli.utils.misc import camel_to_snake

logger = logging.getLogger(__name__)


def generate_table_name(
    resource_type: str, resource_subtype: str | None
) -> str:
    """Generate a normalized table name for the FHIR resource.

    Converts the resource type and optional subtype from CamelCase to
    snake_case and concatenates them with an underscore.

    Args:
        resource_type: The FHIR resource type, e.g., "Patient" or "Observation".
        resource_subtype: Optional subtype, e.g., "Component" or "Performer".

    Returns:
        The normalized table name string.
    """
    table_name = camel_to_snake(resource_type)
    if resource_subtype:
        table_name = f"{table_name}_{camel_to_snake(resource_subtype)}"
    return table_name


class FhirResourceTransformer:
    """Base class for transforming FHIR resources into tabular data.

    Provides methods to evaluate FHIR resources using `sqlonfhir.evaluate`
    based on a `ViewDefinition`. Results are flattened into a list of
    dictionaries suitable for CSV or DataFrame export.

    Attributes:
        resource_type: The FHIR resource type (e.g., "Patient").
        resource_subtype: Optional subtype for nested components.
        table_name: Generated name for the output table or CSV.
        view_definition: SQL-on-FHIR ViewDefinition dict used to extract data.
    """

    def __init__(
        self,
        resource_type: str,
        resource_subtype: str | None,
        view_definition: dict,
    ) -> None:
        """Initialize a FHIR resource transformer.

        Args:
            resource_type: FHIR resource type to transform.
            resource_subtype: Optional subtype for finer-grained naming.
            view_definition: SQL-on-FHIR ViewDefinition defining extraction.
        """
        self.resource_type: str = resource_type
        self.resource_subtype: str | None = resource_subtype
        self.table_name: str = generate_table_name(
            resource_type, resource_subtype
        )
        self.view_definition: dict = view_definition

    def _filter_out_empty_row(self, row_dict: dict[str, Any]) -> dict[str, Any]:
        """Remove row where all non-ID columns are empty or None.

        Args:
            row_dicts: List of row dictionaries produced by evaluation.

        Returns:
            Filtered list of dictionaries with at least one non-empty column.
        """
        id_col = "id"
        foreign_key_col = f"{camel_to_snake(self.resource_type)}_id"

        if not all(
            str(row_dict.get(c)) in {"", "None"}
            for c in row_dict
            if c not in {id_col, foreign_key_col}
        ):
            return row_dict
        else:
            return None

    def _resolve_uuid(self, row: dict[str, Any]) -> dict[str, Any]:
        """Replace placeholder or missing UUIDs with generated UUID4 strings.

        Args:
            row_dicts: List of row dictionaries with possible placeholders.

        Returns:
            The same list with UUIDs populated for missing or placeholder values.
        """
        for k, v in row.items():
            if v == "uuid()":
                row[k] = str(uuid.uuid4())
        return row

    def _normalize_value(self, row: dict[str, Any]) -> dict[str, Any]:
        """
        TODO
        """
        for k, v in row.items():
            if isinstance(v, list) and len(v) == 0:
                row[k] = None
        return row

    def _extract_foreign_key_value(self, row: dict[str, Any]) -> dict[str, Any]:
        """
        Extract foreign key value from foreign key column

        Example: Patient/pt-1234 becomes pt-1234
        """
        fk_column = camel_to_snake(self.resource_type) + "_id"
        fk_value = row.get(fk_column)
        if fk_value:
            row[fk_column] = fk_value.split("/")[-1]

        return row

    def transform_resource(
        self, resource_idx: int, resource_dict: dict[str, Any]
    ) -> list[dict[str, Any]]:
        """Apply the ViewDefinition to a single FHIR resource.

        Args:
            resource_idx: Zero-based index of the resource being transformed.
            resource_dict: JSON dict representing a single FHIR resource.

        Returns:
            A list of flattened row dictionaries from sqlonfhir evaluation.
        """
        results = evaluate(
            resources=[resource_dict], view_definition=self.view_definition
        )
        output = []

        # Post-process
        for row in results:
            row = self._filter_out_empty_row(row)
            if not row:
                continue
            self._resolve_uuid(row)
            self._extract_foreign_key_value(row)
            self._normalize_value(row)

            output.append(row)

        logger.info(
            "Transformed %s %s into %s",
            self.resource_type,
            resource_idx,
            pformat(output),
        )
        return output

    def transform_from_ndjson(
        self, ndjson_filepath: str
    ) -> Generator[list[dict[str, Any]], None, None]:
        """Transform an NDJSON file into row dictionaries per FHIR resource.

        Each line in the NDJSON file is parsed and evaluated through
        `transform_resource`, yielding the resulting row dictionaries.

        Args:
            ndjson_filepath: Path to the NDJSON file to transform.

        Yields:
            Lists of dictionaries representing the flattened resource rows.
        """
        with open(ndjson_filepath, "r") as f:
            for i, line in enumerate(f):
                yield self.transform_resource(i, json.loads(line.strip()))

    def transform_from_json(self, json_filepath: str) -> list[dict[str, Any]]:
        """Transform a JSON file of FHIR resources into a tabular structure.

        Loads a single JSON object or array of FHIR resources and applies
        the ViewDefinition transformation to each resource.

        Args:
            json_filepath: Path to the JSON file containing FHIR resources.

        Returns:
            A list of row dictionaries representing transformed resources.

        Raises:
            ValueError: If the transformation yields zero non-empty rows.
        """
        logger.info("Starting %s", type(self).__name__)
        logger.info(pformat(self.view_definition))

        with open(json_filepath, "r") as f:
            data = json.load(f)
            objs = [data] if isinstance(data, dict) else data

        results: list[dict[str, Any]] = []
        for i, resource in enumerate(objs):
            row_dicts = self.transform_resource(i, resource)
            results.extend(row_dicts)

        if not results:
            raise ValueError(
                f"❌ {type(self).__name__} resulted in 0 non-empty rows! "
                "Please check your ViewDefinition for errors."
            )
        return results

    def write_to_csv(
        self, rows: Iterable[dict[str, Any]], csv_filepath: str
    ) -> None:
        """Write an iterable of row dictionaries to a CSV file.

        Opens the output CSV file and writes rows incrementally as they
        are produced. The header is inferred from the first row.

        Args:
            rows: Iterable of dictionaries, each representing one CSV row.
            csv_filepath: Path to the CSV file to write output to.

        Returns:
            None
        """
        writer = None
        with open(csv_filepath, "w", newline="") as csvfile:
            for row in rows:
                if row is None:
                    continue
                if writer is None:
                    fieldnames = list(row.keys())
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                writer.writerow(row)
