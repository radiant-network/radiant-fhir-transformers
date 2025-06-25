"""
FHIR DocumentReference Context FacilityType Coding transformer
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
        "fhir_path": "context.facilityType.coding",
        "columns": {
            "context_facility_type_coding_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "context_facility_type_coding_code": {
                "fhir_key": "code",
                "type": "str",
            },
            "context_facility_type_coding_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class DocumentReferenceContextFacilityTypeCodingTransformer(
    FhirResourceTransformer
):
    """
    Transformer class for the 'DocumentReference' resource in FHIR, focusing on the 'context.facilityType.coding' element.

    This class transforms FHIR DocumentReference JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'context.facilityType.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('DocumentReference').
        subtype (str): Specifies the sub-element of the resource to focus on ('context_facility_type_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the DocumentReferenceContextFacilityTypeCodingTransformer instance with the resource type 'DocumentReference',
            subtype 'context_facility_type_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "DocumentReference",
            "context_facility_type_coding",
            TRANSFORM_SCHEMA,
        )
