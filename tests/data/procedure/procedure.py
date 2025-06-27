"""
Test helper class for FHIR resource type Procedure
"""

import json

from radiant_fhir_transform_cli.transform.classes.procedure import (
    ProcedureTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .procedure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "resource_type": "Procedure",
        "id": "f201",
        "status": "completed",
        "status_reason_text": "Treatment completed",
        "category_text": "Ordered Procedures",
        "code_text": None,
        "subject_reference": "f201",
        "subject_type": None,
        "subject_display": "Roel",
        "encounter_reference": "f202",
        "encounter_type": None,
        "encounter_display": "Roel's encounter on January 28th, 2013",
        "performed_date_time": None,
        "performed_period_start": "2013-01-28T13:31:00+01:00",
        "performed_period_end": "2013-01-28T14:27:00+01:00",
        "performed_string": None,
        "performed_age_value": None,
        "performed_age_unit": None,
        "performed_age_system": None,
        "performed_age_code": None,
        "performed_range_low_value": None,
        "performed_range_low_unit": None,
        "performed_range_low_system": None,
        "performed_range_low_code": None,
        "performed_range_high_value": None,
        "performed_range_high_unit": None,
        "performed_range_high_system": None,
        "performed_range_high_code": None,
        "recorder_reference": None,
        "recorder_type": None,
        "recorder_display": None,
        "asserter_reference": "eOJIO17tsdF3l7OssxPihIg3",
        "asserter_type": "Practitioner",
        "asserter_display": None,
        "location_reference": None,
        "location_type": None,
        "location_display": None,
        "outcome_text": None,
        "procedure_raw_json": json.dumps(RESOURCE),
    }
]


class ProcedureTestHelper(FhirResourceTestHelper):
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
    resource_subtype = None
    transformer = ProcedureTransformer
    expected_table_name = "procedure"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
