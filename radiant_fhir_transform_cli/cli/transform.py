"""
Commands to transform nested FHIR resource dicts into flat dicts representing
rows in a CSV file
"""

import logging
from typing import Optional

import click

from radiant_fhir_transform_cli.config.log import init_logger

logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--input-filepath",
    required=True,
    help="Path to .ndjson or .json file containg FHIR resources",
)
@click.option(
    "--output-filepath",
    required=True,
    help="Path where csv files will be written",
)
def transform(
    input_filepath: str,
    output_filepath: Optional[str],
):
    """
    Transform a JSON or NDJSON file containing nested FHIR JSON objects
    into rows in a CSV file
    """
    init_logger()

    try:
        logger.info("Transform from %s to %s", input_filepath, output_filepath)
    except Exception as e:
        logger.exception("❌ Failed to transform FHIR JSON data to csv!")
        raise e
