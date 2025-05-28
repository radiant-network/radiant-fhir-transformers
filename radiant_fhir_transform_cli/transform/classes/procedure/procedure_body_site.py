"""
FHIR Procedure BodySite transformer
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
            "procedure_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "bodySite",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "body_site_coding": {"fhir_key": "coding", "type": "str"},
            "body_site_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class ProcedureBodySiteTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Procedure' resource in FHIR, focusing on the 'bodySite' element.

    This class transforms FHIR Procedure JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'bodySite' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Procedure').
        subtype (str): Specifies the sub-element of the resource to focus on ('body_site').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ProcedureBodySiteTransformer instance with the resource type 'Procedure',
            subtype 'body_site', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Procedure", "body_site", TRANSFORM_SCHEMA)
