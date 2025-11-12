"""
FHIR MedicationDispense Substitution Responsible Party transformer
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
        "fhir_path": "substitution.responsibleParty",
        "columns": {
            "substitution_responsible_party_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "substitution_responsible_party_type": {
                "fhir_key": "type",
                "type": "str",
            },
            "substitution_responsible_party_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class MedicationDispenseSubstitutionResponsiblePartyTransformer(
    FhirResourceTransformer
):
    """
    A transformer class for the 'MedicationDispense' resource in FHIR, focusing on the 'substitution.responsibleParty' element.

    This class transforms FHIR MedicationDispense JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'substitution.responsibleParty' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('MedicationDispense').
        subtype (str): Specifies the sub-element of the resource to focus on ('substitution_responsible_party').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the MedicationDispenseSubstitutionResponsiblePartyTransformer instance with the resource type 'MedicationDispense',
            subtype 'substitution_responsible_party', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "MedicationDispense",
            "substitution_responsible_party",
            TRANSFORM_SCHEMA,
        )
