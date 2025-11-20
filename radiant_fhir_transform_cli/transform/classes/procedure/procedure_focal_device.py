"""FHIR Procedure focal_device transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_focal_device",
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
                    "name": "procedure_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "focalDevice",
            "column": [
                {
                    "name": "focal_device_action_text",
                    "path": "action.text",
                    "type": "string",
                },
                {
                    "name": "focal_device_manipulated_reference",
                    "path": "manipulated.reference",
                    "type": "string",
                },
                {
                    "name": "focal_device_manipulated_type",
                    "path": "manipulated.type",
                    "type": "string",
                },
                {
                    "name": "focal_device_manipulated_display",
                    "path": "manipulated.display",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEach": "action.coding",
                    "column": [
                        {
                            "name": "focal_device_action_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "focal_device_action_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "focal_device_action_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class ProcedureFocalDeviceTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Procedure", "focal_device", VIEW_DEFINITION)
