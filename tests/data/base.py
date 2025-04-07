

class FhirResourceTestHelper:

    resource_type = None

    def __init__(self, resource_payload, expected_transform_output):
        self.resource = resource_payload
        self.expected_output = expected_transform_output
