"""
Commands to transform nested FHIR resource dicts into flat dicts representing
rows in a CSV file
"""

import os
import logging
from typing import Optional

import click

from radiant_fhir_transform_cli.config.log import init_logger
from radiant_fhir_transform_cli.transform.classes import transformers

logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--output-filepath",
    help="Path where csv files will be written",
)
@click.option(
    "--input-filepath",
    required=True,
    help="Path to .ndjson or .json file containg FHIR resources",
)
@click.option(
    "--resource-type",
    required=True,
    type=click.Choice(transformers.keys()),
    help="Type of resource in the input file (e.g. Patient, Specimen) to "
    "transform",
)
def transform(
    resource_type: str,
    input_filepath: str,
    output_filepath: Optional[str],
):
    """
    Transform a JSON or NDJSON file containing nested FHIR JSON objects
    into rows in a CSV file
    """
    init_logger()

    if not output_filepath:
        output_filepath = os.path.join(os.getcwd(), resource_type + ".csv")

    try:
        # Instantiate transformer class based on resource type
        cls = transformers.get(resource_type)
        transformer = cls()

        # Transform json or ndjson file
        if input_filepath.endswith(".ndjson"):
            rows = transformer.transform_from_ndjson(input_filepath)
        elif input_filepath.endswith(".json"):
            rows = transformer.transform_from_json(input_filepath)
        else:
            raise click.BadParameter(
                "❌ Input files may only be JSON or NDJSON files"
            )

        # Write to csv
        transformer.write_to_csv(rows, output_filepath)

    except Exception as e:
        logger.exception("❌ Failed to transform FHIR JSON data to csv!")
        raise e
