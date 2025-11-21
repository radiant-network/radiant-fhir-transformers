"""
Test helper class for FHIR resource type List
"""

from radiant_fhir_transform_cli.transform.classes.list import (
    ListTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .list_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "med-list",
        "resource_type": "List",
        "status": "current",
        "mode": "changes",
        "title": "Current Medication List",
        "code_text": "Medication Review",
        "subject_reference": "Patient/example",
        "subject_type": None,
        "subject_display": None,
        "encounter_reference": "Encounter/example",
        "encounter_type": None,
        "encounter_display": None,
        "date": "2013-11-20T23:10:23+11:00",
        "source_reference": "Patient/example",
        "source_type": None,
        "source_display": None,
        "ordered_by_text": None,
        "empty_reason_text": "The patient is not on any medications",
    },
]


class ListTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'List' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'List' resource.

    It predefines the resource type as 'List'
    and initializes the resource with the specific 'List' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'List'.
        resource (dict): The raw FHIR 'List' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'List' resource payload.
    """

    resource_type = "List"
    resource_subtype = None
    transformer = ListTransformer
    expected_table_name = "list"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
