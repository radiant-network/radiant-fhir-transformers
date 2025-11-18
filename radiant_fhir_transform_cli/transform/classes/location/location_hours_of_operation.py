"""FHIR Location hours_of_operation transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Location",
    "name": "location_hours_of_operation",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "location_id", "path": "id", "type": "string"},
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {
                    "name": "hours_of_operation_days_of_week",
                    "path": "hoursOfOperation.daysOfWeek",
                    "type": "string",
                },
                {
                    "name": "hours_of_operation_all_day",
                    "path": "hoursOfOperation.allDay",
                    "type": "string",
                },
                {
                    "name": "hours_of_operation_opening_time",
                    "path": "hoursOfOperation.openingTime",
                    "type": "string",
                },
                {
                    "name": "hours_of_operation_closing_time",
                    "path": "hoursOfOperation.closingTime",
                    "type": "string",
                },
            ]
        }
    ],
}


class LocationHoursOfOperationTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Location", "hours_of_operation", VIEW_DEFINITION)
