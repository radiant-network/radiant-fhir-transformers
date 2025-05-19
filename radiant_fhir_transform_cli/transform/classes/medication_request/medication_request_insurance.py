"""
FHIR MedicationRequest Insurance transformer
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
        "fhir_path": "insurance",
        "fhir_reference": "insurance_reference",
        "columns": {
            "insurance_reference": {"fhir_key": "reference", "type": "str"},
            "insurance_type": {"fhir_key": "type", "type": "str"},
            "insurance_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class MedicationRequestInsuranceTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'MedicationRequest' resource in FHIR, focusing on the 'insurance' element.

    This class transforms FHIR MedicationRequest JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'insurance' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('MedicationRequest').
        subtype (str): Specifies the sub-element of the resource to focus on ('insurance').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the MedicationRequestInsuranceTransformer instance with the resource type 'MedicationRequest',
            subtype 'insurance', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("MedicationRequest", "insurance", TRANSFORM_SCHEMA)
