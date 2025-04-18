"""
List of FHIR ndjson to dict transformers
"""

from radiant_fhir_transform_cli.transform.classes.observation import (
    ObservationCategoryCodingTransformer,
    ObservationComponentTransformer,
    ObservationExtensionTransformer,
    ObservationTransformer,
)
from radiant_fhir_transform_cli.transform.classes.observation.observation_code_coding import (
    ObservationCodeCodingTransformer,
)
from radiant_fhir_transform_cli.transform.classes.patient import (
    PatientTransformer,
)

# Map FHIR resource type to its transformer class
transformers = {
    "Patient": [PatientTransformer],
    "Observation": [
        ObservationTransformer,
        ObservationCategoryCodingTransformer,
        ObservationCodeCodingTransformer,
        ObservationComponentTransformer,
        ObservationExtensionTransformer,
    ],
}
