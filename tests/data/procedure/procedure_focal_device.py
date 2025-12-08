"""
Test helper class for FHIR resource type Procedure subtype FocalDevice
"""

from radiant_fhir_transform_cli.transform.classes.procedure import (
    ProcedureFocalDeviceTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .procedure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "focal_device_action_coding_system": "http://snomed.info/sct",
        "focal_device_action_coding_code": "231361000",
        "focal_device_action_coding_display": " Attention to catheter (procedure)",
        "focal_device_action_text": None,
        "focal_device_manipulated_reference": "Device/manipulated",
        "focal_device_manipulated_type": None,
        "focal_device_manipulated_display": None,
        "id": "06470103-0b2a-4834-8b50-28937d04eed3",
        "procedure_id": "f201",
    },
]


class ProcedureFocalDeviceTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Procedure' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Procedure' resource.

    It predefines the resource type as 'Procedure'
    and initializes the resource with the specific 'Procedure' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Procedure'.

        resource (dict): The raw FHIR 'Procedure' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Procedure' resource payload.
    """

    resource_type = "Procedure"
    resource_subtype = "focal_device"
    transformer = ProcedureFocalDeviceTransformer
    expected_table_name = "procedure_focal_device"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
