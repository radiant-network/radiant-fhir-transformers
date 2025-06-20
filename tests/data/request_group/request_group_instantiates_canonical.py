"""
Test helper class for FHIR resource type RequestGroup subtype InstantiatesCanonical
"""

from radiant_fhir_transform_cli.transform.classes.request_group import (
    RequestGroupInstantiatesCanonicalTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .request_group_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "request_group_id": "kdn5-example",
        "instantiates_canonical": "PlanDefinition/KDN5",
    },
]


class RequestGroupInstantiatesCanonicalTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'RequestGroup' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'RequestGroup' resource.

    It predefines the resource type as 'RequestGroup'
    and initializes the resource with the specific 'RequestGroup' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'RequestGroup'.
        resource (dict): The raw FHIR 'RequestGroup' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'RequestGroup' resource payload.
    """

    resource_type = "RequestGroup"
    resource_subtype = "instantiates_canonical"
    transformer = RequestGroupInstantiatesCanonicalTransformer
    expected_table_name = "request_group_instantiates_canonical"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
