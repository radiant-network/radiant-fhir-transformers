"""FHIR Organization contact transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Organization",
    "name": "organization_contact",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "organization_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "contact",
            "column": [
                {
                    "name": "contact_purpose_coding",
                    "path": "purpose.coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "contact_purpose_text",
                    "path": "purpose.text",
                    "type": "string",
                },
                {
                    "name": "contact_name_use",
                    "path": "name.use",
                    "type": "string",
                },
                {
                    "name": "contact_name_text",
                    "path": "name.text",
                    "type": "string",
                },
                {
                    "name": "contact_name_family",
                    "path": "name.family",
                    "type": "string",
                },
                {
                    "name": "contact_name_given",
                    "path": "name.given",
                    "type": "string",
                },
                {
                    "name": "contact_name_prefix",
                    "path": "name.prefix",
                    "type": "string",
                },
                {
                    "name": "contact_name_suffix",
                    "path": "name.suffix",
                    "type": "string",
                },
                {
                    "name": "contact_name_period_start",
                    "path": "name.period.start",
                    "type": "dateTime",
                },
                {
                    "name": "contact_name_period_end",
                    "path": "name.period.end",
                    "type": "dateTime",
                },
                {
                    "name": "contact_telecom",
                    "path": "telecom",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "contact_address_use",
                    "path": "address.use",
                    "type": "string",
                },
                {
                    "name": "contact_address_type",
                    "path": "address.type",
                    "type": "string",
                },
                {
                    "name": "contact_address_text",
                    "path": "address.text",
                    "type": "string",
                },
                {
                    "name": "contact_address_line",
                    "path": "address.line",
                    "type": "string",
                },
                {
                    "name": "contact_address_city",
                    "path": "address.city",
                    "type": "string",
                },
                {
                    "name": "contact_address_district",
                    "path": "address.district",
                    "type": "string",
                },
                {
                    "name": "contact_address_state",
                    "path": "address.state",
                    "type": "string",
                },
                {
                    "name": "contact_address_postal_code",
                    "path": "address.postalCode",
                    "type": "string",
                },
                {
                    "name": "contact_address_country",
                    "path": "address.country",
                    "type": "string",
                },
                {
                    "name": "contact_address_period_start",
                    "path": "address.period.start",
                    "type": "dateTime",
                },
                {
                    "name": "contact_address_period_end",
                    "path": "address.period.end",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class OrganizationContactTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Organization", "contact", VIEW_DEFINITION)
