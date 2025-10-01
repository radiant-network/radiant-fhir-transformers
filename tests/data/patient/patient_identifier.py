"""
Test helper class for FHIR resource type Organization subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.patient import (
    PatientIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .patient import RESOURCE

EXPECTED_OUTPUT = [
    {
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        "identifier_use": "usual",
        "identifier_type_text": "CEID",
        "identifier_system": "urn:oid:1.2.840.114350.1.13.20.3.7.3.688884.100",
        "identifier_value": "CP2VXPJ1R6VX4LG",
        "identifier_period_start": None,
        "identifier_period_end": None,
        "identifier_value_extension": None,
    },
    {
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        "identifier_use": "usual",
        "identifier_type_text": "EPI",
        "identifier_system": "urn:oid:2.16.840.7.740741.2",
        "identifier_value": "82001496",
        "identifier_period_start": None,
        "identifier_period_end": None,
        "identifier_value_extension": None,
    },
    {
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        "identifier_use": "usual",
        "identifier_type_text": "EXTERNAL",
        "identifier_system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.698084",
        "identifier_value": "Z8201491",
        "identifier_period_start": None,
        "identifier_period_end": None,
        "identifier_value_extension": None,
    },
    {
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        "identifier_use": "usual",
        "identifier_type_text": "FHIR",
        "identifier_system": "http://open.epic.com/FHIR/StructureDefinition/patient-dstu2-fhir-id",
        "identifier_value": "Tu46VewHQTgHXc3sFCHUHh4O.MtOYlDMts1gZ9ximNigB",
        "identifier_period_start": None,
        "identifier_period_end": None,
        "identifier_value_extension": None,
    },
    {
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        "identifier_use": "usual",
        "identifier_type_text": "FHIR STU3",
        "identifier_system": "http://open.epic.com/FHIR/StructureDefinition/patient-fhir-id",
        "identifier_value": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        "identifier_period_start": None,
        "identifier_period_end": None,
        "identifier_value_extension": None,
    },
    {
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        "identifier_use": "usual",
        "identifier_type_text": "INTERNAL",
        "identifier_system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.698084",
        "identifier_value": "Z8201491",
        "identifier_period_start": None,
        "identifier_period_end": None,
        "identifier_value_extension": None,
    },
    {
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        "identifier_use": "usual",
        "identifier_type_text": "MYCHARTLOGIN",
        "identifier_system": "urn:oid:1.2.840.114350.1.13.20.3.7.3.878082.110",
        "identifier_value": "BETTY123",
        "identifier_period_start": None,
        "identifier_period_end": None,
        "identifier_value_extension": None,
    },
    {
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        "identifier_use": "usual",
        "identifier_type_text": "WPRINTERNAL",
        "identifier_system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.878082",
        "identifier_value": "482",
        "identifier_period_start": None,
        "identifier_period_end": None,
        "identifier_value_extension": None,
    },
    {
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        "identifier_use": "usual",
        "identifier_type_text": None,
        "identifier_system": "https://open.epic.com/FHIR/StructureDefinition/PayerMemberId",
        "identifier_value": "JKADJD",
        "identifier_period_start": None,
        "identifier_period_end": None,
        "identifier_value_extension": None,
    },
    {
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        "identifier_use": "usual",
        "identifier_type_text": None,
        "identifier_system": "urn:oid:2.16.840.1.113883.4.1",
        "identifier_value": None,
        "identifier_period_start": None,
        "identifier_period_end": None,
        "identifier_value_extension": [
            {
                "valueString": "xxx-xx-xxxx",
                "url": "http://hl7.org/fhir/StructureDefinition/rendered-value",
            }
        ],
    },
]


class PatientIdentifierTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Patient' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Patient' resource.

    It predefines the resource type as 'Patient'
    and initializes the resource with the specific 'Patient' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Patient'.

        resource (dict): The raw FHIR 'Patient' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Patient' resource payload.
    """

    resource_type = "Patient"
    resource_subtype = "identifier"
    transformer = PatientIdentifierTransformer
    expected_table_name = "patient_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
