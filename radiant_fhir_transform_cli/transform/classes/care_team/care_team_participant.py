"""
FHIR CareTeam Participant transformer
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
        "fhir_path": "participant",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "participant_role_coding": {
                "fhir_key": "role.coding",
                "type": "str",
            },
            "participant_role_text": {"fhir_key": "role.text", "type": "str"},
            "participant_member_reference": {
                "fhir_key": "member.reference",
                "type": "str",
            },
            "participant_member_type": {
                "fhir_key": "member.type",
                "type": "str",
            },
            "participant_member_display": {
                "fhir_key": "member.display",
                "type": "str",
            },
            "participant_on_behalf_of_reference": {
                "fhir_key": "onBehalfOf.reference",
                "type": "str",
            },
            "participant_on_behalf_of_type": {
                "fhir_key": "onBehalfOf.type",
                "type": "str",
            },
            "participant_on_behalf_of_display": {
                "fhir_key": "onBehalfOf.display",
                "type": "str",
            },
            "participant_period_start": {
                "fhir_key": "period.start",
                "type": "datetime",
            },
            "participant_period_end": {
                "fhir_key": "period.end",
                "type": "datetime",
            },
        },
    },
]


class CareTeamParticipantTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'CareTeam' resource in FHIR, focusing on the 'participant' element.

    This class transforms FHIR CareTeam JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'participant' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('CareTeam').
        subtype (str): Specifies the sub-element of the resource to focus on ('participant').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the CareTeamParticipantTransformer instance with the resource type 'CareTeam',
            subtype 'participant', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("CareTeam", "participant", TRANSFORM_SCHEMA)
