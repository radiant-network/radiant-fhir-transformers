"""
Test CLI
"""

from click.testing import CliRunner

from radiant_fhir_transform_cli.cli.transform import *


def test_cli():
    """
    Test placeholder
    """
    runner = CliRunner()
    result = runner.invoke(
        transform,
        [
            "--input-filepath",
            "foo",
            "--output-filepath",
            "bar",
        ],
    )
    assert result.exit_code == 0
