"""
FHIR MedicationRequest SupportingInformation transformer
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
        "fhir_path": "supportingInformation",
        "fhir_reference": "supporting_information_reference",
        "columns": {
            "supporting_information_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "supporting_information_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class MedicationRequestSupportingInformationTransformer(
    FhirResourceTransformer
):
    """
    A transformer class for the 'MedicationRequest' resource in FHIR, focusing on the 'supportingInformation' element.

    This class transforms FHIR MedicationRequest JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'supportingInformation' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('MedicationRequest').
        subtype (str): Specifies the sub-element of the resource to focus on ('supporting_information').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the MedicationRequestSupportingInformationTransformer instance with the resource type 'MedicationRequest',
            subtype 'supporting_information', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "MedicationRequest", "supporting_information", TRANSFORM_SCHEMA
        )
