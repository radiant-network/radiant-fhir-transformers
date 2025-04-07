"""
FHIR Resource Test Helpers

The `FhirResourceTestHelper` class serves as a base helper for testing the
transformation of any FHIR resource by storing the resource payload and its
expected transformation output.
"""


class FhirResourceTestHelper:
    """
    A helper class for testing FHIR resource transformations.

    This class is designed to assist in testing the transformation of FHIR
    resource payloads by storing the resource data and its expected
    transformation output.

    Attributes:
        resource_type (str or None): The type of FHIR resource being tested,
          which defaults to None.

        resource (dict): The raw FHIR resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          resource payload.
    """

    resource_type = None

    def __init__(self, resource_payload, expected_transform_output):
        self.resource = resource_payload
        self.expected_output = expected_transform_output
