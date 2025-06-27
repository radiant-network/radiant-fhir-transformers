"""
Test helper class for FHIR resource type Immunization
"""

import json

from radiant_fhir_transform_cli.transform.classes.immunization import (
    ImmunizationTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .immunization_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "example",
        "resource_type": "Immunization",
        "status": "completed",
        "status_reason_text": None,
        "vaccine_code_text": "Fluvax (Influenza)",
        "patient_reference": "example",
        "patient_type": None,
        "patient_display": None,
        "encounter_reference": "example",
        "encounter_type": None,
        "encounter_display": None,
        "occurrence_date_time": "2013-01-10",
        "occurrence_string": None,
        "recorded": "2013-01-10",
        "primary_source": True,
        "report_origin_text": "Written Record",
        "location_reference": "1",
        "location_type": None,
        "location_display": None,
        "manufacturer_reference": "hl7",
        "manufacturer_type": None,
        "manufacturer_display": None,
        "lot_number": "AAJN11K",
        "expiration_date": "2015-02-15",
        "site_text": None,
        "route_text": None,
        "dose_quantity_value": 5,
        "dose_quantity_unit": None,
        "dose_quantity_system": "http://unitsofmeasure.org",
        "dose_quantity_code": "mg",
        "is_subpotent": True,
        "funding_source_text": None,
        "immunization_raw_json": json.dumps(RESOURCE),
    }
]


class ImmunizationTestHelper(FhirResourceTestHelper):
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
    resource_subtype = None
    transformer = ImmunizationTransformer
    expected_table_name = "immunization"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
