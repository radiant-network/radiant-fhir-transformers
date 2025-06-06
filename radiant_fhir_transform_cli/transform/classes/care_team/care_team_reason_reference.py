"""
FHIR CareTeam ReasonReference transformer
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
            "care_team_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "reasonReference",
        "fhir_reference": "reason_reference_reference",
        "columns": {
            "reason_reference_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "reason_reference_type": {"fhir_key": "type", "type": "str"},
            "reason_reference_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class CareTeamReasonReferenceTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'CareTeam' resource in FHIR, focusing on the 'reasonReference' element.

    This class transforms FHIR CareTeam JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'reasonReference' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('CareTeam').
        subtype (str): Specifies the sub-element of the resource to focus on ('reason_reference').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the CareTeamReasonReferenceTransformer instance with the resource type 'CareTeam',
            subtype 'reason_reference', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("CareTeam", "reason_reference", TRANSFORM_SCHEMA)
