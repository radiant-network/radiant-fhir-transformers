"""
FHIR MedicationRequest Substitution AllowedCodeableConcept Coding transformer
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
        "fhir_path": "substitution.allowedCodeableConcept.coding",
        "columns": {
            "substitution_allowed_codeable_concept_coding_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "substitution_allowed_codeable_concept_coding_code": {
                "fhir_key": "code",
                "type": "str",
            },
            "substitution_allowed_codeable_concept_coding_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class MedicationRequestSubstitutionAllowedCodeableConceptCodingTransformer(
    FhirResourceTransformer
):
    """
    A transformer class for the 'MedicationRequest' resource in FHIR, focusing on the 'substitution.allowedCodeableConcept.coding' element.

    This class transforms FHIR MedicationRequest JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'substitution.allowedCodeableConcept.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('MedicationRequest').
        subtype (str): Specifies the sub-element of the resource to focus on ('substitution_allowed_codeable_concept_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the MedicationRequestSubstitutionAllowedCodeableConceptCodingTransformer instance with the resource type 'MedicationRequest',
            subtype 'substitution_allowed_codeable_concept_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "MedicationRequest",
            "substitution_allowed_codeable_concept_coding",
            TRANSFORM_SCHEMA,
        )
