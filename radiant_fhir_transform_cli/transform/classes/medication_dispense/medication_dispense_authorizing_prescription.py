"""
FHIR MedicationDispense AuthorizingPrescription transformer
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
        "fhir_path": "authorizingPrescription",
        "columns": {
            "authorizing_prescription_reference": {"fhir_key": "reference", "type": "str"},
            "authorizing_prescription_type": {"fhir_key": "type", "type": "str"},
            "authorizing_prescription_display": {"fhir_key": "display", "type": "str"},
        },
    },
]

class MedicationDispenseAuthorizingPrescriptionTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'MedicationDispense' resource in FHIR, focusing on the 'authorizingPrescription' element.

    This class transforms FHIR MedicationDispense JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'authorizingPrescription' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('MedicationDispense').
        subtype (str): Specifies the sub-element of the resource to focus on ('authorizing_prescription').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the MedicationDispenseAuthorizingPrescriptionTransformer instance with the resource type 'MedicationDispense',
            subtype 'authorizing_prescription', and the specified transformation dictionary.
    """
    
    def __init__(self):
        super().__init__("MedicationDispense", "authorizing_prescription", TRANSFORM_SCHEMA)