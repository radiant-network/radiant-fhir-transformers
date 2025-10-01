"""
FHIR CareTeam ManagingOrganization transformer
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
        "fhir_path": "managingOrganization",
        "fhir_reference": "managing_organization_reference",
        "columns": {
            "managing_organization_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "managing_organization_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class CareTeamManagingOrganizationTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'CareTeam' resource in FHIR, focusing on the 'managingOrganization' element.

    This class transforms FHIR CareTeam JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'managingOrganization' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('CareTeam').
        subtype (str): Specifies the sub-element of the resource to focus on ('managing_organization').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the CareTeamManagingOrganizationTransformer instance with the resource type 'CareTeam',
            subtype 'managing_organization', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("CareTeam", "managing_organization", TRANSFORM_SCHEMA)
