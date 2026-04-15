"""
Test helper class for FHIR resource type MedicationRequest subtype ReasonCode
"""

from radiant_fhir_transform_cli.transform.classes.medication_request import (
    MedicationRequestReasonCodeTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_request_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "reason_code_coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "50820005",
                "display": "Cytopenia (finding)",
            },
            {
                "system": "http://hl7.org/fhir/sid/icd-9-cm",
                "code": "289.9",
                "display": "Unspecified diseases of blood and blood-forming organs",
            },
            {
                "system": "http://hl7.org/fhir/sid/icd-10-cm",
                "code": "D75.9",
                "display": "Disease of blood and blood-forming organs, unspecified",
            },
        ],
        "reason_code_text": "Cytopenia",
        "id": "1c62f09f-69ce-4008-954b-03db4da721e1",
        "medication_request_id": "medrx0301",
    },
    {
        "reason_code_coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "370388006",
                "display": "Patient immunocompromised (finding)",
            },
            {
                "system": "http://hl7.org/fhir/sid/icd-9-cm",
                "code": "279.9",
                "display": "Unspecified disorder of immune mechanism",
            },
            {
                "system": "http://hl7.org/fhir/sid/icd-10-cm",
                "code": "D84.9",
                "display": "Immunodeficiency, unspecified",
            },
        ],
        "reason_code_text": "Immunocompromised state",
        "id": "1c62f09f-69ce-4008-954b-03db4da721e1",
        "medication_request_id": "medrx0301",
    },
    {
        "reason_code_coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "243815002",
                "display": "Prevention status (finding)",
            },
            {
                "system": "http://hl7.org/fhir/sid/icd-9-cm",
                "code": "V07.8",
                "display": "Other specified prophylactic or treatment measure",
            },
            {
                "system": "http://hl7.org/fhir/sid/icd-10-cm",
                "code": "Z29.89",
                "display": "Encounter for other specified prophylactic measures",
            },
        ],
        "reason_code_text": "Need for pneumocystis prophylaxis",
        "id": "1c62f09f-69ce-4008-954b-03db4da721e1",
        "medication_request_id": "medrx0301",
    },
    {
        "reason_code_coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "443333004",
                "display": "Medulloblastoma (disorder)",
            },
            {
                "system": "http://hl7.org/fhir/sid/icd-9-cm",
                "code": "191.6",
                "display": "Malignant neoplasm of cerebellum NOS",
            },
            {
                "system": "http://hl7.org/fhir/sid/icd-10-cm",
                "code": "C71.6",
                "display": "Malignant neoplasm of cerebellum",
            },
        ],
        "reason_code_text": "Medulloblastoma",
        "id": "1c62f09f-69ce-4008-954b-03db4da721e1",
        "medication_request_id": "medrx0301",
    },
]


class MedicationRequestReasonCodeTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'MedicationRequest' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'MedicationRequest' resource.

    It predefines the resource type as 'MedicationRequest'
    and initializes the resource with the specific 'MedicationRequest' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'MedicationRequest'.

        resource (dict): The raw FHIR 'MedicationRequest' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'MedicationRequest' resource payload.
    """

    resource_type = "MedicationRequest"
    resource_component = "reason_code"
    transformer = MedicationRequestReasonCodeTransformer
    expected_table_name = "medication_request_reason_code"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
