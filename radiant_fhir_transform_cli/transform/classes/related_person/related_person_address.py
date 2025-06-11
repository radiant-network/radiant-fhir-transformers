"""
FHIR RelatedPerson Address transformer
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
        "fhir_path": "address",
        "columns": {
            "address_use": {"fhir_key": "use", "type": "str"},
            "address_type": {"fhir_key": "type", "type": "str"},
            "address_text": {"fhir_key": "text", "type": "str"},
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "address_line": {"fhir_key": "line", "type": "str"},
            "address_city": {"fhir_key": "city", "type": "str"},
            "address_district": {"fhir_key": "district", "type": "str"},
            "address_state": {"fhir_key": "state", "type": "str"},
            "address_postal_code": {"fhir_key": "postalCode", "type": "str"},
            "address_country": {"fhir_key": "country", "type": "str"},
            "address_period_start": {
                "fhir_key": "period.start",
                "type": "datetime",
            },
            "address_period_end": {
                "fhir_key": "period.end",
                "type": "datetime",
            },
        },
    },
]


class RelatedPersonAddressTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'RelatedPerson' resource in FHIR, focusing on the 'address' element.

    This class transforms FHIR RelatedPerson JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'address' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('RelatedPerson').
        subtype (str): Specifies the sub-element of the resource to focus on ('address').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the RelatedPersonAddressTransformer instance with the resource type 'RelatedPerson',
            subtype 'address', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("RelatedPerson", "address", TRANSFORM_SCHEMA)
