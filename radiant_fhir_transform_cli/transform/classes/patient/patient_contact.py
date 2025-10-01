"""
FHIR Patient Contact transformer
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
            "patient_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "contact",
        "columns": {
            "contact_relationship": {"fhir_key": "relationship", "type": "str"},
            "contact_name_use": {"fhir_key": "name.use", "type": "str"},
            "contact_name_text": {"fhir_key": "name.text", "type": "str"},
            "contact_name_family": {"fhir_key": "name.family", "type": "str"},
            "contact_name_given": {"fhir_key": "name.given", "type": "str"},
            "contact_name_prefix": {"fhir_key": "name.prefix", "type": "str"},
            "contact_name_suffix": {"fhir_key": "name.suffix", "type": "str"},
            "contact_name_period_start": {
                "fhir_key": "name.period.start",
                "type": "datetime",
            },
            "contact_name_period_end": {
                "fhir_key": "name.period.end",
                "type": "datetime",
            },
            "contact_telecom": {"fhir_key": "telecom", "type": "str"},
            "contact_address_use": {"fhir_key": "address.use", "type": "str"},
            "contact_address_type": {"fhir_key": "address.type", "type": "str"},
            "contact_address_text": {"fhir_key": "address.text", "type": "str"},
            "contact_address_line": {"fhir_key": "address.line", "type": "str"},
            "contact_address_city": {"fhir_key": "address.city", "type": "str"},
            "contact_address_district": {
                "fhir_key": "address.district",
                "type": "str",
            },
            "contact_address_state": {
                "fhir_key": "address.state",
                "type": "str",
            },
            "contact_address_postal_code": {
                "fhir_key": "address.postalCode",
                "type": "str",
            },
            "contact_address_country": {
                "fhir_key": "address.country",
                "type": "str",
            },
            "contact_address_period_start": {
                "fhir_key": "address.period.start",
                "type": "datetime",
            },
            "contact_address_period_end": {
                "fhir_key": "address.period.end",
                "type": "datetime",
            },
            "contact_gender": {"fhir_key": "gender", "type": "str"},
            "contact_organization_reference": {
                "fhir_key": "organization.reference",
                "type": "str",
            },
            "contact_organization_type": {
                "fhir_key": "organization.type",
                "type": "str",
            },
            "contact_organization_identifier": {
                "fhir_key": "organization.identifier",
                "type": "str",
            },
            "contact_organization_display": {
                "fhir_key": "organization.display",
                "type": "str",
            },
            "contact_period_start": {
                "fhir_key": "period.start",
                "type": "datetime",
            },
            "contact_period_end": {
                "fhir_key": "period.end",
                "type": "datetime",
            },
        },
    },
]


class PatientContactTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Patient' resource in FHIR, focusing on the 'contact' element.

    This class transforms FHIR Coverage JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'contact' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Patient').
        subtype (str): Specifies the sub-element of the resource to focus on ('contact').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the PatientContactTransformer instance with the resource type 'Patient',
            subtype 'contact', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Patient", "contact", TRANSFORM_SCHEMA)
