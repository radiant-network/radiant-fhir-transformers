"""
FHIR MedicationRequest ReasonCode transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
    {
        "fhir_path": None,
        "columns": {
            "id": {"fhir_key": None, "type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "medication_request_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "reasonCode",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            # "reason_code_coding": {"fhir_key": "coding", "type": "str"},
            "reason_code_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class MedicationRequestReasonCodeTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'MedicationRequest' resource in FHIR, focusing on the 'reasonCode' element.

    This class transforms FHIR MedicationRequest JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'reasonCode' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('MedicationRequest').
        subtype (str): Specifies the sub-element of the resource to focus on ('reason_code').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the MedicationRequestReasonCodeTransformer instance with the resource type 'MedicationRequest',
            subtype 'reason_code', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("MedicationRequest", "reason_code", TRANSFORM_SCHEMA)
