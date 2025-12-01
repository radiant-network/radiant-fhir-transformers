import json

from radiant_fhir_transform_cli.transform.classes.raw_fhir import (
    RawFhirResourceTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .raw_fhir_resource import RESOURCE

raw_fhir_str = json.dumps(RESOURCE)

expected_output = [
    {
        "id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "resource_type": "Observation",
        "json": RESOURCE,
    }
]


class RawFhirResourceTestHelper(FhirResourceTestHelper):
    resource_type = "fhir_resource"
    resource_subtype = None
    transformer = RawFhirResourceTransformer
    expected_table_name = "fhir_resource"

    def __init__(self):
        super().__init__(RESOURCE, expected_output)
