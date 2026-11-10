class FhirTransformError(Exception):
    """Base exception for FHIR transformation errors."""


class InvalidTransformConfigError(FhirTransformError):
    """Exception for invalid transformation configurations."""
