"""
Test helper class for FHIR resource type Immunization subtype SubpotentReason
"""

from radiant_fhir_transform_cli.transform.classes.immunization import (
    ImmunizationSubpotentReasonTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .immunization_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "immunization_id": "example",
        "subpotent_reason_coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/immunization-subpotent-reason",
                "code": "partial",
                "display": "Partial Dose",
            }
        ],
        "subpotent_reason_text": None,
    },
]


class ImmunizationSubpotentReasonTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Immunization' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Immunization' resource.

    It predefines the resource type as 'Immunization'
    and initializes the resource with the specific 'Immunization' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Immunization'.
        resource (dict): The raw FHIR 'Immunization' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'Immunization' resource payload.
    """

    resource_type = "Immunization"
    resource_subtype = "subpotent_reason"
    transformer = ImmunizationSubpotentReasonTransformer
    expected_table_name = "immunization_subpotent_reason"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
