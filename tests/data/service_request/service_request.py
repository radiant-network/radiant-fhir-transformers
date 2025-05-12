"""
Test helper class for FHIR resource type ServiceRequest
"""

from radiant_fhir_transform_cli.transform.classes.service_request.service_request import (
    ServiceRequestTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .service_request_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "di_abcd_efg",
        "resource_type": "ServiceRequest",
        "text_status":"generated",
        "status": "active",
        "intent": "original-order",
        "priority":"routine",
        "do_not_perform":True,
        "code_text": "Chest CT",
        "quantity_quantity_value":"5",
        "quantity_quantity_comparator": "something",
        "quantity_quantity_unit": "acres",
        "quantity_quantity_system": "imperial_units",
        "quantity_quantity_code": "konami",    
        "quantity_ratio_numerator_value": 1,  
        "quantity_ratio_numerator_comparator": 5,  
        "quantity_ratio_numerator_unit":  "gallons",  
        "quantity_ratio_numerator_system":  "metric",  
        "quantity_ratio_numerator_code": "gl",  
        "quantity_ratio_denominator_value":  2,  
        "quantity_ratio_denominator_comparator":  5,  
        "quantity_ratio_denominator_unit": "gallons",  
        "quantity_ratio_denominator_system":  "metric",  
        "quantity_ratio_denominator_code":  "gl",   
        "quantity_range_low_value": 1,   
        "quantity_range_low_unit": "part",   
        "quantity_range_high_value": 10,   
        "quantity_range_high_unit": "part",   
        "subject_reference": "dicom.example.pt",
        "subject_display": "Judy Test",
        "encounter_reference": "example",
        "encounter_display": "1234encounter",
        "occurrence_date_time":"2013-05-08T09:33:27+07:00",
        "occurrence_period_start": "2013-05-08",
        "occurrence_period_end": "2013-05-09",
        "occurrence_timing_repeat_count": 20,
        "occurrence_timing_repeat_count_max": 30,
        "occurrence_timing_repeat_frequency": 3,
        "occurrence_timing_repeat_period": 1,
        "occurrence_timing_repeat_period_unit": "wk",
        "as_needed_boolean": False,
        "as_needed_codeable_concept_text": "as needed text example",
        "authored_on":"2014-02-14",
        "requester_reference": "example.doc",
        "requester_display": "Dr. Adam Careful",
        "performer_type_coding": [{'system': 'http://orionhealth.com/fhir/apps/specialties', 'code': 'ent', 'display': 'ENT'}],
        "performer_type_text": "Ear Nose and Throat",
        "patient_instruction": "Start with 30kg 10-15 repetitions for three sets and increase in increments of 5kg when you feel ready",
    }
]


class ServiceRequestTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'ServiceRequest' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'ServiceRequest' resource.

    It predefines the resource type as 'ServiceRequest'
    and initializes the resource with the specific 'ServiceRequest' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'ServiceRequest'.

        resource (dict): The raw FHIR 'ServiceRequest' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'ServiceRequest' resource payload.
    """

    resource_type = "ServiceRequest"
    resource_subtype = None
    transformer = ServiceRequestTransformer
    expected_table_name = "service_request"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
