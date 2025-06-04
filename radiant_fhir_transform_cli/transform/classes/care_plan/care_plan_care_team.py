"""
FHIR CarePlan careTeam transformer
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
            "care_plan_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "careTeam",
        "columns": {
            "care_team_reference": {"fhir_key": "reference", "type": "str"},
            "care_team_display": {"fhir_key": "display", "type": "str"},
            "care_team_type": {"fhir_key": "type", "type": "str"},
        },
    },
]


class CarePlanCareTeamTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'CarePlan' resource in FHIR, focusing on the 'careTeam' element.

    This class transforms FHIR CarePlan JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'careTeam' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('CarePlan').
        subtype (str): Specifies the sub-element of the resource to focus on ('care_team').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the CarePlanCareTeamTransformer instance with the resource type 'CarePlan',
            subtype 'care_team', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("CarePlan", "care_team", TRANSFORM_SCHEMA)
