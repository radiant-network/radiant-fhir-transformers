"""
Test helper class for FHIR resource type Procedure subtype BodySite
"""

from radiant_fhir_transform_cli.transform.classes.procedure import (
    ProcedureBodySiteTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .procedure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "body_site_coding_system": "http://snomed.info/sct",
        "body_site_coding_code": "272676008",
        "body_site_coding_display": "Sphenoid bone",
        "body_site_text": None,
        "id": "6382bbfc-c4d3-47f7-90b7-58c554005049",
        "procedure_id": "f201",
    },
]


class ProcedureBodySiteTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Procedure' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Procedure' resource.

    It predefines the resource type as 'Procedure'
    and initializes the resource with the specific 'Procedure' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Procedure'.

        resource (dict): The raw FHIR 'Procedure' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Procedure' resource payload.
    """

    resource_type = "Procedure"
    resource_subtype = "body_site"
    transformer = ProcedureBodySiteTransformer
    expected_table_name = "procedure_body_site"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
