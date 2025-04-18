"""
Test helper class for FHIR resource type Observation
"""

from radiant_fhir_transform_cli.transform.classes.observation.observation import (
    ObservationTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .observation_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "resource_type": "Observation",
        "status": "final",
        "code_text": "Rapid Sars-CoV-2",
        "subject_reference": "evrlLhFNe5BfHZQD39Kr9nfIA0e.TcZOdE0gOPoRXlGs3",
        "subject_display": "CareEverywhere,Sammy",
        "encounter_reference": "e.mnIF2M9LQgwkDzhr2PCKA3",
        "encounter_identifier_use": "usual",
        "encounter_identifier_system": "urn:oid:1.2.840.114350.1.13.20.3.7.3.698084.8",
        "encounter_identifier_value": "8200106334",
        "encounter_display": "Hospital Encounter",
        "value_quantity_value": None,
        "value_quantity_unit": None,
        "value_quantity_code": None,
        "value_quantity_system": None,
        "value_codeable_concept_text": "Negative",
        "value_range_low_value": None,
        "value_range_low_unit": None,
        "value_range_high_value": None,
        "value_range_high_unit": None,
        "value_ratio_numerator_value": None,
        "value_ratio_numerator_unit": None,
        "value_ratio_numerator_code": None,
        "value_ratio_denominator_value": None,
        "value_ratio_denominator_unit": None,
        "value_ratio_denominator_code": None,
        "value_string": None,
        "value_boolean": None,
        "value_integer": None,
        "effective_datetime": "2024-01-29T16:46:00Z",
        "issued": "2024-01-29T16:46:57Z",
        "effective_period_start": None,
        "effective_period_end": None,
        "specimen_reference": "eofvi8EpxgTC9958OEt3Xuw3",
        "specimen_display": "Specimen 24U-ID-0290004",
    }
]


class ObservationTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Observation' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Observation' resource.

    It predefines the resource type as 'Observation'
    and initializes the resource with the specific 'Observation' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Observation'.

        resource (dict): The raw FHIR 'Observation' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Observation' resource payload.
    """

    resource_type = "Observation"
    resource_subtype = None
    transformer = ObservationTransformer

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
