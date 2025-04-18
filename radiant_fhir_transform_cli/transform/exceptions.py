class FhirTransformError(Exception):
    """Base exception for FHIR transformation errors."""

    pass


class InvalidTransformConfigError(FhirTransformError):
    """Exception for invalid transformation configurations."""

    pass
