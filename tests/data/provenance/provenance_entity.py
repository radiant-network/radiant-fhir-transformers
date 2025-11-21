"""
Test helper class for FHIR resource type Provenance subtype Entity
"""

from radiant_fhir_transform_cli.transform.classes.provenance import (
    ProvenanceEntityTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .provenance_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "entity_role": "source",
        "entity_what_reference": "DocumentReference/entity",
        "entity_what_type": None,
        "entity_what_display": "CDA Document in XDS repository",
        "entity_agent": None,
        "id": "8d9b783a-25ed-469e-b4fe-4be9e7931c7b",
        "provenance_id": "provenance",
    },
]


class ProvenanceEntityTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Provenance' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Provenance' resource.

    It predefines the resource type as 'Provenance'
    and initializes the resource with the specific 'Provenance' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Provenance'.

        resource (dict): The raw FHIR 'Provenance' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Provenance' resource payload.
    """

    resource_type = "Provenance"
    resource_subtype = "entity"
    transformer = ProvenanceEntityTransformer
    expected_table_name = "provenance_entity"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
