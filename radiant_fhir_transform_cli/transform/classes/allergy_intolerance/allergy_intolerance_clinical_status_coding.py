"""
FHIR AllergyIntolerance Clinical Status Coding transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
    {
        "fhir_path": None,
        "columns": {
            "id": {"type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "allergy_intolerance_id": {"type": "str"},
        },
    },
    {
        "fhir_path": "clinicalStatus.coding",
        "columns": {
            "clinical_status_coding_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "clinical_status_coding_code": {"fhir_key": "code", "type": "str"},
            "clinical_status_coding_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class AllergyIntoleranceClinicalStatusCodingTransformer(
    FhirResourceTransformer
):
    """
    A transformer class for the 'AllergyIntolerance' resource in FHIR, focusing on the 'clinicalStatus.coding' element.
    This class transforms FHIR AllergyIntolerance JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'clinicalStatus.coding' field.
    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('AllergyIntolerance').
        subtype (str): Specifies the sub-element of the resource to focus on ('clinical_status_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.
    Methods:
        __init__():
            Initializes the AllergyIntoleranceClinicalStatusCodingTransformer instance with the resource type 'AllergyIntolerance',
            subtype 'clinical_status_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "AllergyIntolerance", "clinical_status_coding", TRANSFORM_SCHEMA
        )
