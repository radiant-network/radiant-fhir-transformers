"""
FHIR DocumentReference Context PracticeSetting Coding transformer
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
            "document_reference_id": {"type": "str"},
        },
    },
    {
        "fhir_path": "context.practiceSetting.coding",
        "columns": {
            "context_practice_setting_coding_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "context_practice_setting_coding_code": {
                "fhir_key": "code",
                "type": "str",
            },
            "context_practice_setting_coding_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class DocumentReferenceContextPracticeSettingCodingTransformer(
    FhirResourceTransformer
):
    """
    Transformer class for the 'DocumentReference' resource in FHIR, focusing on the 'context.practiceSetting.coding' element.

    This class transforms FHIR DocumentReference JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'context.practiceSetting.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('DocumentReference').
        subtype (str): Specifies the sub-element of the resource to focus on ('context_practice_setting_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the DocumentReferenceContextPracticeSettingCodingTransformer instance with the resource type 'DocumentReference',
            subtype 'context_practice_setting_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "DocumentReference",
            "context_practice_setting_coding",
            TRANSFORM_SCHEMA,
        )
