"""
Commands to transform nested FHIR resource dicts into flat dicts representing
rows in a CSV file
"""

import json
import logging
import os
import time
from datetime import datetime
from pprint import pformat
from textwrap import indent

import click

from radiant_fhir_transform_cli.config.log import init_logger
from radiant_fhir_transform_cli.transform.classes import transformers

logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--output-dir",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=str),
    help="Directory where csv files will be written",
)
@click.option(
    "--input-filepath",
    required=True,
    help="Path to .ndjson or .json file containg FHIR resources",
)
@click.option(
    "--resource-type",
    required=True,
    type=click.Choice(list(transformers.keys())),
    help="Type of resource in the input file (e.g. Patient, Specimen) to "
    "transform",
)
def transform(
    resource_type: str,
    input_filepath: str,
    output_dir: str | None,
):
    """
    Transform a JSON or NDJSON file containing nested FHIR JSON objects
    into rows in a CSV file
    """
    init_logger()

    if not output_dir:
        output_dir = os.path.join(os.getcwd())

    logger.info("Output CSV files in %s", output_dir)

    try:
        # Instantiate transformer class based on resource type

        resource_transformers = transformers.get(resource_type)

        if not resource_transformers:
            logger.info(
                "⚠️ Resource type: %s does not have any transformers",
                resource_type,
            )
            return

        total_time = time.perf_counter()
        total_pr = time.process_time()
        report: dict[str, float] = {}
        for rt in resource_transformers:
            transformer = rt()

            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

            transfomer_name = transformer.table_name

            output_filepath = f"{output_dir}/{transfomer_name}-{timestamp}.csv"

            start_time = time.perf_counter()

            # Transform json or ndjson file
            if input_filepath.endswith(".ndjson"):
                rows = transformer.transform_from_ndjson(input_filepath)
            elif input_filepath.endswith(".json"):
                rows = transformer.transform_from_json(input_filepath)
            else:
                raise click.BadParameter(
                    "❌ Input files may only be JSON or NDJSON files"
                )
            duration = time.perf_counter() - start_time
            report[transfomer_name] = duration
            logger.info(
                "⏲️ Transformed  %s %.4f seconds",
                transfomer_name,
                duration,
            )

            # Write to csv
            transformer.write_to_csv(rows, output_filepath)
            logger.info(
                "Wrote %s results to %s", str(rt.__name__), output_filepath
            )
        logger.info(
            "✅ Total Time %.4f sec total CPU time %.4f",
            (time.perf_counter() - total_time),
            (time.process_time() - total_pr),
        )

        logger.info("%s", json.dumps(report, indent=2))

    except Exception as e:
        logger.exception("❌ Failed to transform FHIR JSON data to csv!")
        raise e
