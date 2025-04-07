"""
Entrypoint for the CLI

All commands are initialized here
"""

import click

from radiant_fhir_transform_cli.cli.transform import *


@click.group()
def fhir():
    """
    Group of CLI commands related transforming FHIR data
    """


@click.group()
@click.version_option()
def main():
    """
    A CLI tool for tranforming FHIR resources in ndjson files to csv files

    This method does not need to be implemented. cli is the root group that all
    subcommands will implicitly be part of.
    """


# Transform command
fhir.add_command(transform)

# Add command groups to the root CLI
main.add_command(fhir)
