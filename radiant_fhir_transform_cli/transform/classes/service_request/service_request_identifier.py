"""
FHIR ServiceRequest Identifier transformer
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
            "service_request_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "identifier",
        "columns": {
            "identifier_type_text": {"fhir_key": "type.text", "type": "str"},
            "identifier_system": {"fhir_key": "system", "type": "str"},
            "identifier_value": {"fhir_key": "value", "type": "str"},
            "identifier_period": {"fhir_key": "period", "type": "str"},
            "identifier_assigner_organization_reference": {"fhir_key": "assigner.organization.reference", "type": "str"},
            "identifier_assigner_organization_type": {"fhir_key": "assigner.organization.type", "type": "str"},
            "identifier_assigner_organization_display": {"fhir_key": "assigner.organization.display", "type": "str"},
            "identifier_assigner_organization_identifier": {"fhir_key": "assigner.organization.identifier", "type": "str"},            
        },
    },
]


class ServiceRequestIdentifierTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'ServiceRequest' resource in FHIR, focusing on the 'identifier' element.

    This class transforms FHIR ServiceRequest JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'identifier' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('ServiceRequest').
        subtype (str): Specifies the sub-element of the resource to focus on ('identifier').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ServiceRequestCodeCodingTransformer instance with the resource type 'ServiceRequest',
            subtype 'identifier', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("ServiceRequest", "identifier", TRANSFORM_SCHEMA)
