"""
Test helper class for FHIR resource type Specimen
"""

from radiant_fhir_transform_cli.transform.classes.specimen.specimen import (
    SpecimenTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .specimen_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "101",
        "resource_type": "Specimen",
        "status": "available",
        "accession_identifier_use": None,
        "accession_identifier_system": "http://lab.acme.org/specimens/2011",
        "accession_identifier_value": "X352356",
        "accession_identifier_period": None,
        "accession_identifier_assigner_reference": None,
        "accession_identifier_assigner_display": None,
        "type_text":"venous blood",
        "subject_reference":"example",
        "subject_display":"Peter Patient",
        "received_time": "2011-03-04T07:03:00Z",
        "collection_collector_reference": "example",
        "collection_collector_display": None,
        "collection_collected_date_time": "2011-05-30T06:15:00Z",
        "collection_collected_period_start": None,
        "collection_collected_period_end": None,
        "collection_duration_value": None,
        "collection_duration_comparator": None,
        "collection_duration_unit": None,
        "collection_duration_system": None,
        "collection_duration_code": None,
        "collection_quantity_value": 6,
        "collection_quantity_unit": "mL",
        "collection_quantity_system":None,
        "collection_quantity_code":None,
        "collection_method_text": "Venous Line",
        "collection_body_site_text": "Right median cubital vein", 
        "collection_fasting_status_duration_value": None,
        "collection_fasting_status_duration_comparator": None,
        "collection_fasting_status_duration_unit": None,
        "collection_fasting_status_duration_system": None,
        "collection_fasting_status_duration_code": None,
        "collection_fasting_status_text": None

    }
]


class SpecimenTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Specimen' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Specimen' resource.

    It predefines the resource type as 'Specimen'
    and initializes the resource with the specific 'Specimen' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Observation'.

        resource (dict): The raw FHIR 'Specimen' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Specimen' resource payload.
    """

    resource_type = "Specimen"
    resource_subtype = None
    transformer = SpecimenTransformer
    expected_table_name = "specimen"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
