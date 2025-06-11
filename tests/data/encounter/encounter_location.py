"""
Test helper class for FHIR resource type Encounter subtype location
"""

from radiant_fhir_transform_cli.transform.classes.encounter.encounter_location import (
    EncounterLocationTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .encounter_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "encounter_id": "f203",
        "location_location_reference": None,
        "location_location_type": None,
        "location_location_display": "Example",
        "location_status": "active",
        "location_physical_type_coding_code": None,
        "location_physical_type_coding_system": None,
        "location_physical_type_coding_display": None,
        "location_physical_type_text": None,
        "location_period_start": "2017-02-01T07:15:00+10:00",
        "location_period_end": "2017-02-01T08:45:00+10:00",
    }
]


class EncounterLocationTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Encounter' resource,
    specifically for the 'location' subtype.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Encounter' resource
    with a focus on the 'location' field.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Encounter'.
        resource_subtype (str): The subtype of the FHIR resource being tested, set to 'location'.
        transformer (type): The class responsible for transforming the FHIR resource.
        expected_table_name (str): The name of the table expected after transformation.

    """

    resource_type = "Encounter"
    resource_subtype = "location"
    transformer = EncounterLocationTransformer
    expected_table_name = "encounter_location"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
