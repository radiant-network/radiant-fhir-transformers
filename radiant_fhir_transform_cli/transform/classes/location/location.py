"""FHIR Location transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Location",
    "name": "location",
    "status": "active",
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "id",
                    "type": "string",
                },
                {
                    "name": "resource_type",
                    "path": "resourceType",
                    "type": "string",
                },
                {
                    "name": "status",
                    "path": "status",
                    "type": "string",
                },
                {
                    "name": "operational_status_system",
                    "path": "operationalStatus.system",
                    "type": "string",
                },
                {
                    "name": "operational_status_code",
                    "path": "operationalStatus.code",
                    "type": "string",
                },
                {
                    "name": "operational_status_display",
                    "path": "operationalStatus.display",
                    "type": "string",
                },
                {
                    "name": "name",
                    "path": "name",
                    "type": "string",
                },
                {
                    "name": "description",
                    "path": "description",
                    "type": "string",
                },
                {
                    "name": "mode",
                    "path": "mode",
                    "type": "string",
                },
                {
                    "name": "address_use",
                    "path": "address.use",
                    "type": "string",
                },
                {
                    "name": "address_type",
                    "path": "address.type",
                    "type": "string",
                },
                {
                    "name": "address_text",
                    "path": "address.text",
                    "type": "string",
                },
                {
                    "name": "address_city",
                    "path": "address.city",
                    "type": "string",
                },
                {
                    "name": "address_district",
                    "path": "address.district",
                    "type": "string",
                },
                {
                    "name": "address_state",
                    "path": "address.state",
                    "type": "string",
                },
                {
                    "name": "address_postal_code",
                    "path": "address.postalCode",
                    "type": "string",
                },
                {
                    "name": "address_country",
                    "path": "address.country",
                    "type": "string",
                },
                {
                    "name": "address_period_start",
                    "path": "address.period.start",
                    "type": "dateTime",
                },
                {
                    "name": "address_period_end",
                    "path": "address.period.end",
                    "type": "dateTime",
                },
                {
                    "name": "physical_type_text",
                    "path": "physicalType.text",
                    "type": "string",
                },
                {
                    "name": "position_longitude",
                    "path": "position.longitude",
                    "type": "string",
                },
                {
                    "name": "position_latitude",
                    "path": "position.latitude",
                    "type": "string",
                },
                {
                    "name": "position_altitude",
                    "path": "position.altitude",
                    "type": "string",
                },
                {
                    "name": "managing_organization_reference",
                    "path": "managingOrganization.reference",
                    "type": "string",
                },
                {
                    "name": "managing_organization_type",
                    "path": "managingOrganization.type",
                    "type": "string",
                },
                {
                    "name": "managing_organization_display",
                    "path": "managingOrganization.display",
                    "type": "string",
                },
                {
                    "name": "part_of_reference",
                    "path": "partOf.reference",
                    "type": "string",
                },
                {
                    "name": "part_of_type",
                    "path": "partOf.type",
                    "type": "string",
                },
                {
                    "name": "part_of_display",
                    "path": "partOf.display",
                    "type": "string",
                },
                {
                    "name": "availability_exceptions",
                    "path": "availabilityExceptions",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEach": "address.line",
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


class LocationTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Location", None, VIEW_DEFINITION)
