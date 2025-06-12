"""
FHIR RelatedPerson Name transformer
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
            "related_person_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "name",
        "columns": {
            "name_use": {"fhir_key": "use", "type": "str"},
            "name_text": {"fhir_key": "text", "type": "str"},
            "name_family": {"fhir_key": "family", "type": "str"},
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "name_given": {"fhir_key": "given", "type": "str"},
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "name_prefix": {"fhir_key": "prefix", "type": "str"},
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "name_suffix": {"fhir_key": "suffix", "type": "str"},
            "name_period_start": {
                "fhir_key": "period.start",
                "type": "datetime",
            },
            "name_period_end": {"fhir_key": "period.end", "type": "datetime"},
        },
    },
]


class RelatedPersonNameTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'RelatedPerson' resource in FHIR, focusing on the 'name' element.

    This class transforms FHIR RelatedPerson JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'name' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('RelatedPerson').
        subtype (str): Specifies the sub-element of the resource to focus on ('name').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the RelatedPersonNameTransformer instance with the resource type 'RelatedPerson',
            subtype 'name', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("RelatedPerson", "name", TRANSFORM_SCHEMA)
