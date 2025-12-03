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
from dataclasses import dataclass
from pprint import pformat
from typing import Any

from sqlonfhir import evaluate

from radiant_fhir_transform_cli.utils.misc import camel_to_snake

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ColumnMetaData:
    """
    Represents a single column definition extracted from a ViewDefinition node.
    """

    name: str
    type: str | None


def generate_table_name(
    resource_type: str, resource_subtype: str | None
) -> str:
    """Generate a normalized table name for a FHIR resource.

    Converts the resource type and optional subtype from CamelCase to
    snake_case, concatenating them with an underscore if a subtype is present.

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
    based on a provided `ViewDefinition`. Results are flattened into a list
    of dictionaries suitable for CSV or DataFrame export.

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

    def _filter_out_empty_row(
        self, row_dict: dict[str, Any]
    ) -> dict[str, Any] | None:
        """Filter out a row where all non-ID columns are empty or None.

        Rows that contain only ID or foreign key values and have no populated
        data fields are excluded from the output.

        Args:
            row_dict: A single row dictionary produced by SQL-on-FHIR evaluation.

        Returns:
            The same row dictionary if it contains at least one non-empty column;
            otherwise, returns ``None``.
        """
        id_col = "id"
        foreign_key_col = f"{camel_to_snake(self.resource_type)}_id"

        if not all(
            str(row_dict.get(c)) in {"", "None"}
            for c in row_dict
            if c not in {id_col, foreign_key_col}
        ):
            return row_dict
        return None

    def _resolve_uuid(self, row: dict[str, Any]) -> dict[str, Any]:
        """Replace placeholder UUID strings with generated UUID4 values.

        Fields that contain the literal value ``"uuid()"`` are replaced with
        a newly generated UUID4 string.

        Args:
            row: A single row dictionary with possible UUID placeholders.

        Returns:
            The same row dictionary with all placeholder UUIDs replaced.
        """
        uuid_value = row.get("id")
        if uuid_value and uuid_value == "uuid()":
            row["id"] = str(uuid.uuid4())
        return row

    def _normalize_value(self, row: dict[str, Any]) -> dict[str, Any]:
        """Normalize values in a row to ensure consistent representation.

        Converts empty lists to ``None`` to avoid JSON serialization issues
        and maintain a consistent null representation.

        Args:
            row: A row dictionary representing transformed values.

        Returns:
            The same row dictionary with normalized values.
        """
        for k, v in row.items():
            if isinstance(v, list) and len(v) == 0:
                row[k] = None
        return row

    def _extract_foreign_key_value(self, row: dict[str, Any]) -> dict[str, Any]:
        """Extract the ID portion from a FHIR reference string.

        For foreign key columns like ``Patient/pt-1234``, this method extracts
        and replaces the value with only the ID segment (e.g., ``pt-1234``).

        Args:
            row: A row dictionary containing a foreign key column.

        Returns:
            The same row dictionary with the foreign key value normalized.
        """
        fk_column = camel_to_snake(self.resource_type) + "_id"
        fk_value = row.get(fk_column)
        if fk_value:
            row[fk_column] = fk_value.split("/")[-1]
        return row

    def transform_resources(
        self, resources: list[dict]
    ) -> list[dict[str, Any]]:
        """Apply the ViewDefinition to a single FHIR resource.

        Evaluates the given resource using SQL-on-FHIR, filters out empty
        rows, normalizes values, extracts foreign keys, and replaces any
        UUID placeholders.

        Args:
            resource_idx: Index of the resource being transformed (for logging).
            resource_dict: JSON dictionary representing a single FHIR resource.

        Returns:
            A list of flattened and post-processed row dictionaries.
        """
        try:
            results = evaluate(
                resources=resources, view_definition=self.view_definition
            )
        except Exception:
            logger.error(
                "❌ Transform failed for %s %s. Subtype: %s",
                len(resources),
                self.resource_type,
                self.resource_subtype,
            )
            raise

        output: list[dict[str, Any]] = []

        for row in results:
            row = self._filter_out_empty_row(row)
            if not row:
                continue
            self._resolve_uuid(row)
            self._extract_foreign_key_value(row)
            self._normalize_value(row)
            output.append(row)

        logger.info(
            "🏭 Transformed %s %s. Subtype: %s. Rows: %s",
            len(resources),
            self.resource_type,
            self.resource_subtype,
            len(output),
        )
        return output

    def transform_resource(
        self, resource_idx: int, resource_dict: dict[str, Any]
    ) -> list[dict[str, Any]]:
        """Apply the ViewDefinition to a single FHIR resource.

        Evaluates the given resource using SQL-on-FHIR, filters out empty
        rows, normalizes values, extracts foreign keys, and replaces any
        UUID placeholders.

        Args:
            resource_idx: Index of the resource being transformed (for logging).
            resource_dict: JSON dictionary representing a single FHIR resource.

        Returns:
            A list of flattened and post-processed row dictionaries.
        """
        return self.transform_resources([resource_dict])

    def column_metadata(self) -> list[ColumnMetaData]:
        """
        Recursively extract column metadata from a ViewDefinition-like dictionary.
        """

        def extract_cols(vd: dict[str, Any]) -> list[ColumnMetaData]:
            cols: list[ColumnMetaData] = []

            # Extract columns at this level
            for col in vd.get("column", []):
                cols.append(
                    ColumnMetaData(
                        name=col["name"],
                        type=col.get("type"),
                    )
                )

            # Recurse into nested select blocks
            for child in vd.get("select", []):
                cols.extend(extract_cols(child))
            return cols

        return extract_cols(self.view_definition)

    def transform_from_ndjson(
        self, ndjson_filepath: str
    ) -> list[dict[str, Any]]:
        """Transform an NDJSON file into row dictionaries per FHIR resource.

        Each line of the NDJSON file is parsed and evaluated using
        ``transform_resource``, yielding the transformed rows for each resource.

        Args:
            ndjson_filepath: Path to the NDJSON file containing FHIR resources.

        Yields:
            Lists of row dictionaries representing each transformed resource.
        """
        results = []
        with open(ndjson_filepath, "r") as f:
            rows = [json.loads(line.strip()) for i, line in enumerate(f)]
            self.transform_resources(rows)

        return results

    def transform_from_json(self, json_filepath: str) -> list[dict[str, Any]]:
        """Transform a JSON file of FHIR resources into tabular structures.

        Reads a JSON file containing one or more FHIR resources and applies
        the configured ViewDefinition transformation to each.

        Args:
            json_filepath: Path to the JSON file containing FHIR resources.

        Returns:
            A list of flattened dictionaries representing transformed rows.

        Raises:
            ValueError: If the transformation yields zero non-empty rows.
        """
        logger.info("Starting %s", type(self).__name__)
        logger.info(pformat(self.view_definition))

        with open(json_filepath, "r") as f:
            data = json.load(f)
            objs = [data] if isinstance(data, dict) else data

        results = self.transform_resources(objs)

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
            csv_filepath: Path to the CSV file where output will be written.

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
