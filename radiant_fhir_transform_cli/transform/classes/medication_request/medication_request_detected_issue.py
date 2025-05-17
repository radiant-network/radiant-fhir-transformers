"""
FHIR MedicationRequest DetectedIssue transformer
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
        "fhir_path": "detectedIssue",
        "fhir_reference": "detected_issue_reference",
        "columns": {
            "detected_issue_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "detected_issue_type": {"fhir_key": "type", "type": "str"},
            "detected_issue_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class MedicationRequestDetectedIssueTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'MedicationRequest' resource in FHIR, focusing on the 'detectedIssue' element.

    This class transforms FHIR MedicationRequest JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'detectedIssue' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('MedicationRequest').
        subtype (str): Specifies the sub-element of the resource to focus on ('detected_issue').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the MedicationRequestDetectedIssueTransformer instance with the resource type 'MedicationRequest',
            subtype 'detected_issue', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "MedicationRequest", "detected_issue", TRANSFORM_SCHEMA
        )
