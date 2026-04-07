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
        "reason_code_text": "Cytopenia",
        "reason_code_coding_system": "http://snomed.info/sct",
        "reason_code_coding_code": "50820005",
        "reason_code_coding_display": "Cytopenia (finding)",
        "id": "1c62f09f-69ce-4008-954b-03db4da721e1",
        "medication_request_id": "medrx0301",
    },
    {
        "reason_code_text": "Cytopenia",
        "reason_code_coding_system": "http://hl7.org/fhir/sid/icd-9-cm",
        "reason_code_coding_code": "289.9",
        "reason_code_coding_display": "Unspecified diseases of blood and blood-forming organs",
        "id": "1c62f09f-69ce-4008-954b-03db4da721e1",
        "medication_request_id": "medrx0301",
    },
    {
        "reason_code_text": "Cytopenia",
        "reason_code_coding_system": "http://hl7.org/fhir/sid/icd-10-cm",
        "reason_code_coding_code": "D75.9",
        "reason_code_coding_display": "Disease of blood and blood-forming organs, unspecified",
        "id": "1c62f09f-69ce-4008-954b-03db4da721e1",
        "medication_request_id": "medrx0301",
    },
    {
        "reason_code_text": "Immunocompromised state",
        "reason_code_coding_system": "http://snomed.info/sct",
        "reason_code_coding_code": "370388006",
        "reason_code_coding_display": "Patient immunocompromised (finding)",
        "id": "7d8faa5b-6257-4031-8586-96423af2e21f",
        "medication_request_id": "medrx0301",
    },
    {
        "reason_code_text": "Immunocompromised state",
        "reason_code_coding_system": "http://hl7.org/fhir/sid/icd-9-cm",
        "reason_code_coding_code": "279.9",
        "reason_code_coding_display": "Unspecified disorder of immune mechanism",
        "id": "7d8faa5b-6257-4031-8586-96423af2e21f",
        "medication_request_id": "medrx0301",
    },
    {
        "reason_code_text": "Immunocompromised state",
        "reason_code_coding_system": "http://hl7.org/fhir/sid/icd-10-cm",
        "reason_code_coding_code": "D84.9",
        "reason_code_coding_display": "Immunodeficiency, unspecified",
        "id": "7d8faa5b-6257-4031-8586-96423af2e21f",
        "medication_request_id": "medrx0301",
    },
    {
        "reason_code_text": "Need for pneumocystis prophylaxis",
        "reason_code_coding_system": "http://snomed.info/sct",
        "reason_code_coding_code": "243815002",
        "reason_code_coding_display": "Prevention status (finding)",
        "id": "b694953e-de96-4948-8564-611b666dcc3e",
        "medication_request_id": "medrx0301",
    },
    {
        "reason_code_text": "Need for pneumocystis prophylaxis",
        "reason_code_coding_system": "http://hl7.org/fhir/sid/icd-9-cm",
        "reason_code_coding_code": "V07.8",
        "reason_code_coding_display": "Other specified prophylactic or treatment measure",
        "id": "b694953e-de96-4948-8564-611b666dcc3e",
        "medication_request_id": "medrx0301",
    },
    {
        "reason_code_text": "Need for pneumocystis prophylaxis",
        "reason_code_coding_system": "http://hl7.org/fhir/sid/icd-10-cm",
        "reason_code_coding_code": "Z29.89",
        "reason_code_coding_display": "Encounter for other specified prophylactic measures",
        "id": "b694953e-de96-4948-8564-611b666dcc3e",
        "medication_request_id": "medrx0301",
    },
    {
        "reason_code_text": "Medulloblastoma",
        "reason_code_coding_system": "http://snomed.info/sct",
        "reason_code_coding_code": "443333004",
        "reason_code_coding_display": "Medulloblastoma (disorder)",
        "id": "7b901194-ecc8-4e38-9cea-570e464b8e46",
        "medication_request_id": "medrx0301",
    },
    {
        "reason_code_text": "Medulloblastoma",
        "reason_code_coding_system": "http://hl7.org/fhir/sid/icd-9-cm",
        "reason_code_coding_code": "191.6",
        "reason_code_coding_display": "Malignant neoplasm of cerebellum NOS",
        "id": "7b901194-ecc8-4e38-9cea-570e464b8e46",
        "medication_request_id": "medrx0301",
    },
    {
        "reason_code_text": "Medulloblastoma",
        "reason_code_coding_system": "http://hl7.org/fhir/sid/icd-10-cm",
        "reason_code_coding_code": "C71.6",
        "reason_code_coding_display": "Malignant neoplasm of cerebellum",
        "id": "7b901194-ecc8-4e38-9cea-570e464b8e46",
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
