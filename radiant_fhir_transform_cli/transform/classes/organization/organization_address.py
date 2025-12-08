"""FHIR Organization address transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Organization",
    "name": "organization_address",
    "status": "active",
    "constant": [
        {
            "name": "id_uuid",
            "valueString": "uuid()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_uuid",
                    "type": "string",
                },
                {
                    "name": "organization_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "address",
            "column": [
                {
                    "name": "address_use",
                    "path": "use",
                    "type": "string",
                },
                {
                    "name": "address_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "address_text",
                    "path": "text",
                    "type": "string",
                },
                {
                    "name": "address_city",
                    "path": "city",
                    "type": "string",
                },
                {
                    "name": "address_district",
                    "path": "district",
                    "type": "string",
                },
                {
                    "name": "address_state",
                    "path": "state",
                    "type": "string",
                },
                {
                    "name": "address_postal_code",
                    "path": "postalCode",
                    "type": "string",
                },
                {
                    "name": "address_country",
                    "path": "country",
                    "type": "string",
                },
                {
                    "name": "address_period_start",
                    "path": "period.start",
                    "type": "dateTime",
                },
                {
                    "name": "address_period_end",
                    "path": "period.end",
                    "type": "dateTime",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "line",
                    "column": [
                        {
                            "name": "address_line",
                            "path": "$this",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class OrganizationAddressTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Organization", "address", VIEW_DEFINITION)
