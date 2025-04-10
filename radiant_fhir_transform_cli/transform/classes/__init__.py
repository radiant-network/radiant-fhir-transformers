"""
List of FHIR ndjson to dict transformers
"""

from radiant_fhir_transform_cli.transform.classes.observation import (
    ObservationTransformer,
)
from radiant_fhir_transform_cli.transform.classes.patient import (
    PatientTransformer,
)

# Map FHIR resource type to its transformer class
transformers = {
    "Patient": PatientTransformer,
    "Observation": ObservationTransformer,
}
