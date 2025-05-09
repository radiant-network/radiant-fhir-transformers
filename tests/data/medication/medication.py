"""
Test helper class for FHIR resource type Medication
"""

from radiant_fhir_transform_cli.transform.classes.medication import (
    MedicationTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "med0301",
        "resource_type": "Medication",
        "code_text": "Vancomycin HCL",
        "status": "active",
        "manufacturer_reference": "#org4",
        "manufacturer_type": "Organization",
        "manufacturer_display": "Organization 4",
        "form_text": "Solution for injection",
        "batch_lot_number": "9494788",
        "batch_expiration_date": "2017-05-22",
    }
]


class MedicationTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Medication' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Medication' resource.

    It predefines the resource type as 'Medication'
    and initializes the resource with the specific 'Medication' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Medication'.

        resource (dict): The raw FHIR 'Medication' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Medication' resource payload.
    """

    resource_type = "Medication"
    resource_subtype = None
    transformer = MedicationTransformer
    expected_table_name = "medication"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
