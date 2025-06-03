"""
FHIR Provenance Signature transformer
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
            "provenance_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "signature",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "signature_type": {"fhir_key": "type", "type": "str"},
            "signature_when": {"fhir_key": "when", "type": "datetime"},
            "signature_who_reference": {
                "fhir_key": "who.reference",
                "type": "str",
            },
            "signature_who_type": {"fhir_key": "who.type", "type": "str"},
            "signature_who_display": {"fhir_key": "who.display", "type": "str"},
            "signature_on_behalf_of_reference": {
                "fhir_key": "onBehalfOf.reference",
                "type": "str",
            },
            "signature_on_behalf_of_type": {
                "fhir_key": "onBehalfOf.type",
                "type": "str",
            },
            "signature_on_behalf_of_display": {
                "fhir_key": "onBehalfOf.display",
                "type": "str",
            },
            "signature_target_format": {
                "fhir_key": "targetFormat",
                "type": "str",
            },
            "signature_sig_format": {"fhir_key": "sigFormat", "type": "str"},
            # TODO: Handling base64Binary Data Types in Transformers (See https://github.com/radiant-network/radiant-fhir-transformers/issues/53)
            # "signature_data": {"fhir_key": "data", "type": "str"},
        },
    },
]


class ProvenanceSignatureTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Provenance' resource in FHIR, focusing on the 'signature' element.

    This class transforms FHIR Provenance JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'signature' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Provenance').
        subtype (str): Specifies the sub-element of the resource to focus on ('signature').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ProvenanceSignatureTransformer instance with the resource type 'Provenance',
            subtype 'signature', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Provenance", "signature", TRANSFORM_SCHEMA)
