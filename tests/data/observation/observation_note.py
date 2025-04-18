"""
Test helper class for FHIR resource type Observation subtype notes
"""

from radiant_fhir_transform_cli.transform.classes.observation import (
    ObservationNoteTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .observation_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "note_text": """This test was developed and its performance characteristics determined by the Children's Hospital of Philadelphia clinical laboratory. The U. S. Food and Drug Administration has not approved or cleared this test; however, FDA clearance or approval is not currently required for clinical use. The results are not intended to be used as the sole means of clinical diagnosis or patient management decisions. This laboratory is certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA-88) as qualified to perform high complexity clinical laboratory testing.\r\nThe 2019 novel coronavirus (SARS-CoV-2) target nucleic acids NOT DETECTED by real-time PCR.\r\n\r\nThis test was developed and its performance characteristics determined by Cepheid. This test has not been FDA cleared or approved. This test has been authorized by the FDA under an Emergency Use Authorization (EUA). This test is only authorized for the duration of time that circumstances exist justifying the authorization of the emergency use of in vitro diagnostic tests for detection of SARS-CoV-2 virus and/or diagnosis of COVID-19 infection under section 564(b)(1) of the Act, 21 U.S.C. 360bbb-3(b)(1), unless the authorization is terminated or revoked sooner. The Children's Hospital of Philadelphia is authorized to perform this test as certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA-88) as qualified to perform high complexity clinical laboratory testing. The results are not intended to be used as the sole means of clinical diagnosis or patient management decision.""",
    },
    {
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "note_text": "Test CHOP",
    },
]


class ObservationNoteTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "extension"
    transformer = ObservationNoteTransformer
    expected_table_name = "observation_note"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
