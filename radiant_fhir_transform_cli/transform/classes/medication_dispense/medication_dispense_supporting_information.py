"""
FHIR MedicationDispense SupportingInformation transformer
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
            "medication_dispense_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "supportingInformation",
        "columns": {
            "supporting_information_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "supporting_information_type": {"fhir_key": "type", "type": "str"},
            "supporting_information_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class MedicationDispenseSupportingInformationTransformer(
    FhirResourceTransformer
):
    """
    A transformer class for the 'MedicationDispense' resource in FHIR, focusing on the 'supportingInformation' element.

    This class transforms FHIR MedicationDispense JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'supportingInformation' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('MedicationDispense').
        subtype (str): Specifies the sub-element of the resource to focus on ('supporting_information').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the MedicationDispenseSupportingInformationTransformer instance with the resource type 'MedicationDispense',
            subtype 'supporting_information', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "MedicationDispense", "supporting_information", TRANSFORM_SCHEMA
        )
