"""
Test helper class for FHIR resource type Specimen subtype container
"""

from radiant_fhir_transform_cli.transform.classes import (
    SpecimenContainerTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .specimen import RESOURCE

EXPECTED_OUTPUT = [
    {
        "container_identifier_value": "48736-15394-75465",
        "container_description": "Green Gel tube",
        "container_type_text": "Vacutainer",
        "container_type_coding": None,
        "container_capacity_value": 10,
        "container_capacity_unit": "mL",
        "container_capacity_system": None,
        "container_capacity_code": None,
        "container_specimen_quantity_value": 6,
        "container_specimen_quantity_unit": "mL",
        "container_specimen_quantity_system": None,
        "container_specimen_quantity_code": None,
        "container_specimen_additive_codeable_concept_text": None,
        "container_specimen_additive_codeable_concept_coding": None,
        "container_specimen_additive_reference_reference": None,
        "container_specimen_additive_reference_display": None,
        "container_specimen_additive_reference_type": None,
        "id": "41b26927-2725-482e-bcd2-92e9c896ff59",
        "specimen_id": "101",
    },
]


class SpecimenContainerTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Specimen' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Specimen' resource.

    It predefines the resource type as 'Specimen'
    and initializes the resource with the specific 'Specimen' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Specimen'.

        resource (dict): The raw FHIR 'Specimen' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Specimen' resource payload.
    """

    resource_type = "Specimen"
    resource_subtype = "container"
    transformer = SpecimenContainerTransformer
    expected_table_name = "specimen_container"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
