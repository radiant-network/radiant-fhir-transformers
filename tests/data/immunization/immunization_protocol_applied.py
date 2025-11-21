"""
Test helper class for FHIR resource type Immunization subtype ProtocolApplied
"""

from radiant_fhir_transform_cli.transform.classes.immunization import (
    ImmunizationProtocolAppliedTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .immunization_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "protocol_applied_target_disease_coding": {
            "system": "http://snomed.info/sct",
            "code": "40468003",
        },
        "protocol_applied_series": "2-dose",
        "protocol_applied_authority_reference": None,
        "protocol_applied_authority_type": None,
        "protocol_applied_authority_display": None,
        "protocol_applied_dose_number_positive_int": 1,
        "protocol_applied_dose_number_string": None,
        "protocol_applied_series_doses_positive_int": None,
        "protocol_applied_series_doses_string": None,
        "id": "f0809a34-4b6b-4a45-b7d3-a4fee39dbaa2",
        "immunization_id": "example",
    },
    {
        "protocol_applied_target_disease_coding": {
            "system": "http://snomed.info/sct",
            "code": "66071002",
        },
        "protocol_applied_series": "3-dose",
        "protocol_applied_authority_reference": None,
        "protocol_applied_authority_type": None,
        "protocol_applied_authority_display": None,
        "protocol_applied_dose_number_positive_int": 2,
        "protocol_applied_dose_number_string": None,
        "protocol_applied_series_doses_positive_int": None,
        "protocol_applied_series_doses_string": None,
        "id": "6e8ccfc1-c0bd-446b-b260-c64db3c41a4c",
        "immunization_id": "example",
    },
]


class ImmunizationProtocolAppliedTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "protocol_applied"
    transformer = ImmunizationProtocolAppliedTransformer
    expected_table_name = "immunization_protocol_applied"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
