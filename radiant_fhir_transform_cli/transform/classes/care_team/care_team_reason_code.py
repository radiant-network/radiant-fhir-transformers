"""
FHIR CareTeam ReasonCode transformer
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
        "fhir_path": "reasonCode",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "reason_code_coding": {"fhir_key": "coding", "type": "str"},
            "reason_code_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class CareTeamReasonCodeTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'CareTeam' resource in FHIR, focusing on the 'reasonCode' element.

    This class transforms FHIR CareTeam JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'reasonCode' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('CareTeam').
        subtype (str): Specifies the sub-element of the resource to focus on ('reason_code').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the CareTeamReasonCodeTransformer instance with the resource type 'CareTeam',
            subtype 'reason_code', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("CareTeam", "reason_code", TRANSFORM_SCHEMA)
