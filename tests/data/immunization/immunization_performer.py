"""
Test helper class for FHIR resource type Immunization subtype Performer
"""

from radiant_fhir_transform_cli.transform.classes.immunization import (
    ImmunizationPerformerTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .immunization_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "immunization_id": "example",
        "performer_function_coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/v2-0443",
                "code": "OP",
            }
        ],
        "performer_function_text": None,
        "performer_actor_reference": "Practitioner/example",
        "performer_actor_type": None,
        "performer_actor_display": None,
    },
    {
        "immunization_id": "example",
        "performer_function_coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/v2-0443",
                "code": "AP",
            }
        ],
        "performer_function_text": None,
        "performer_actor_reference": "Practitioner/example",
        "performer_actor_type": None,
        "performer_actor_display": None,
    },
]


class ImmunizationPerformerTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "performer"
    transformer = ImmunizationPerformerTransformer
    expected_table_name = "immunization_performer"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
