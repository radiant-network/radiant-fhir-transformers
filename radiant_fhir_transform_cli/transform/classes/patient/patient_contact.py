"""FHIR Patient contact transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Patient",
    "name": "patient_contact",
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
                    "name": "patient_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "contact",
            "column": [
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
                {
                    "name": "contact_gender",
                    "path": "gender",
                    "type": "string",
                },
                {
                    "name": "contact_organization_reference",
                    "path": "organization.reference",
                    "type": "string",
                },
                {
                    "name": "contact_organization_type",
                    "path": "organization.type",
                    "type": "string",
                },
                {
                    "name": "contact_organization_identifier",
                    "path": "organization.identifier",
                    "type": "string",
                },
                {
                    "name": "contact_organization_display",
                    "path": "organization.display",
                    "type": "string",
                },
                {
                    "name": "contact_period_start",
                    "path": "period.start",
                    "type": "dateTime",
                },
                {
                    "name": "contact_period_end",
                    "path": "period.end",
                    "type": "dateTime",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "relationship",
                    "column": [
                        {
                            "name": "contact_relationship_text",
                            "path": "text",
                            "type": "string",
                        },
                    ],
                    "select": [
                        {
                            "forEachOrNull": "coding",
                            "column": [
                                {
                                    "name": "contact_relationship_coding_system",
                                    "path": "system",
                                    "type": "string",
                                },
                                {
                                    "name": "contact_relationship_coding_code",
                                    "path": "code",
                                    "type": "string",
                                },
                                {
                                    "name": "contact_relationship_coding_display",
                                    "path": "display",
                                    "type": "string",
                                },
                            ],
                        },
                    ],
                },
                {
                    "forEachOrNull": "telecom",
                    "column": [
                        {
                            "name": "contact_telecom_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "contact_telecom_value",
                            "path": "value",
                            "type": "string",
                        },
                        {
                            "name": "contact_telecom_use",
                            "path": "use",
                            "type": "string",
                        },
                    ],
                },
                {
                    "forEachOrNull": "address.line",
                    "column": [
                        {
                            "name": "contact_address_line",
                            "path": "$this",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class PatientContactTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Patient", "contact", VIEW_DEFINITION)
