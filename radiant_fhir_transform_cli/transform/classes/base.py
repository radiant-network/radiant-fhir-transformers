import json
import logging
from pprint import pformat
from typing import Any, Generator, Iterable, Optional

import pandas
from fhirpathpy import evaluate

logger = logging.getLogger(__name__)


class DataType:
    INTEGER: "int"
    STRING: "str"
    BOOLEAN: "bool"
    DATETIME: "datetime"


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

        if not fhir_path or not isinstance(columns, dict):
            raise ValueError(msg)


def extract_fhir_reference_prefix(fhir_raw_value: Any) -> str:
    if not isinstance(fhir_raw_value, str):
        logger.warning(
            "Incorrect use of fhir_reference field... Must be a string"
        )
        return fhir_raw_value

    return fhir_raw_value.rsplit("/", 1)[-1]


def extract_column_values(
    item: Any, columns_dict: dict, fhir_ref: Optional[str]
) -> dict:
    """Extracts column values from a single FHIR item based on column mappings."""
    if isinstance(item, dict):
        values = {
            col_name: item.get(col_config_dict["fhir_key"])
            for col_name, col_config_dict in columns_dict.items()
        }
        if fhir_ref:
            print(f"fhir reference {fhir_ref}  {values[fhir_ref]}")
            values[fhir_ref] = extract_fhir_reference_prefix(values[fhir_ref])
        return values

    if isinstance(item, (str, int, float, bool)) and len(columns_dict) == 1:
        # TODO exception or log when columsn are more than 1 Create Custom exception
        col_name = next(iter(columns_dict))

        if fhir_ref:
            item = extract_fhir_reference_prefix(item)
        return {col_name: item}

    raise ValueError(
        "Unable to extract columns: unexpected item structure or ambiguous mapping."
    )


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
        base_result = {}
        subtype_results = []
        for config in self.transform_dict:
            fhir_path_expression = config["fhir_path"]
            fhir_reference = config.get("fhir_reference")
            columns_dict: dict = config["columns"]

            raw_items = evaluate(resource_dict, fhir_path_expression)

            # Base case... single result from fhir path
            if isinstance(raw_items, list) and len(raw_items) == 1:
                base_result.update(
                    self._handle_single_result(
                        raw_items[0], columns_dict, fhir_reference
                    )
                )
            # handle subtypes
            elif isinstance(raw_items, list) and len(raw_items) > 1:
                if subtype_results:
                    raise ValueError(
                        "Transformation error... Multi list not supported"
                    )
                subtype_results = self._handle_list_result(
                    raw_items, columns_dict, fhir_reference
                )
            # Unknown Result Type
            else:
                logger.warning(
                    "Unexpected FHIRPath result type %s", pformat(raw_items)
                )
                base_result.update({col: None for col in columns_dict})

        if subtype_results:
            final_results = [
                {**subtype_result, **base_result}
                for subtype_result in subtype_results
            ]
        else:
            final_results = [base_result]

        logger.debug(
            "Transformed %s %s into %s",
            self.resource_type,
            resource_idx,
            pformat(final_results),
        )

        return final_results

    def _handle_single_result(
        self, raw_item: Any, columns_dict: dict, fhir_ref: Optional[str]
    ) -> dict:
        try:
            return extract_column_values(raw_item, columns_dict, fhir_ref)
        except ValueError as e:
            logger.warning(
                "Failed to extract values from %s: %s",
                pformat(raw_item),
                str(e),
            )
        return {col: None for col in columns_dict}

    def _handle_list_result(
        self, raw_items: list, columns_dict: dict, fhir_ref: Optional[str]
    ) -> list[dict]:
        """Handles extraction from multiple FHIRPath results."""
        if not self.resource_subtype:
            raise ValueError(
                "Multiple results from FHIRPath are only supported for subtypes"
            )

        return [
            self._handle_single_result(item, columns_dict, fhir_ref)
            for item in raw_items
        ]

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
