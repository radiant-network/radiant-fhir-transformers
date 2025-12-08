"""
Test helper class for FHIR resource type Provenance subtype Agent
"""

from radiant_fhir_transform_cli.transform.classes.provenance import (
    ProvenanceAgentTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .provenance_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "agent_type_coding_system": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        "agent_type_coding_code": "AUT",
        "agent_type_text": None,
        "agent_role": None,
        "agent_who_reference": "Practitioner/author",
        "agent_who_type": None,
        "agent_who_display": None,
        "agent_on_behalf_of_reference": None,
        "agent_on_behalf_of_type": None,
        "agent_on_behalf_of_display": None,
        "id": "cbd448ba-18a2-41f2-b70d-897b9904e53a",
        "provenance_id": "provenance",
    },
    {
        "agent_type_coding_system": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        "agent_type_coding_code": "DEV",
        "agent_type_text": None,
        "agent_role": None,
        "agent_who_reference": "Device/device",
        "agent_who_type": None,
        "agent_who_display": None,
        "agent_on_behalf_of_reference": None,
        "agent_on_behalf_of_type": None,
        "agent_on_behalf_of_display": None,
        "id": "979c4ab6-8dac-43ac-8628-5a6e2334032a",
        "provenance_id": "provenance",
    },
]


class ProvenanceAgentTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "agent"
    transformer = ProvenanceAgentTransformer
    expected_table_name = "provenance_agent"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
