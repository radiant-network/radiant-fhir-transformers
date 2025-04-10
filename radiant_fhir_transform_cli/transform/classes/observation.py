"""
FHIR Observation transformer

Map nested fields in the Observation resource to keys in a flat dict which
represents a row in a csv file

Transform Dictionary
--------------------
- Keys are output columns in a csv file.

- Values are FHIR path expressions to
  the field value to be extracted from the FHIR JSON object
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

OBSERVATION_CATEGORY = (
    "http://terminology.hl7.org/CodeSystem/observation-category"
)

TRANSFORM_DICT = {
    "id": "id",
    "category": f"category.where(coding.system='{OBSERVATION_CATEGORY}').coding.where(system='{OBSERVATION_CATEGORY}').code",
    "subject_id": "subject.reference",
}


class ObservationTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Observation' resource in FHIR.

    Transform Patient JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_dict (dict): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the ObservationTransformer instance with the resource
            type 'Observation' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Observation", TRANSFORM_DICT)
