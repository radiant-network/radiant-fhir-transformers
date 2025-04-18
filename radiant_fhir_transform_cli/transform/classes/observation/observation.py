"""
FHIR Observation transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

OBSERVATION_CATEGORY = (
    "http://terminology.hl7.org/CodeSystem/observation-category"
)


TRANSFORM_DICT = [
    # Id
    {
        "fhir_path": "id",
        "columns": {"id": {"fhir_key": "id", "type": "str"}},
    },
    {
        "fhir_path": "resourceType",
        "columns": {
            "resource_type": {"fhir_key": "resourceType", "type": "str"}
        },
    },
    {
        "fhir_path": "status",
        "columns": {"status": {"fhir_key": "status", "type": "str"}},
    },
    {
        "fhir_path": "code.text",
        "columns": {
            "code_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "subject",
        "fhir_reference": "subject_reference",
        "columns": {
            "subject_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "subject_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "encounter.reference",
        "fhir_reference": "encounter_reference",
        "columns": {
            "encounter_reference": {
                "fhir_key": "encounter.reference",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "encounter.identifier",
        "columns": {
            "encounter_identifier_use": {"fhir_key": "use", "type": "str"},
            "encounter_identifier_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "encounter_identifier_value": {"fhir_key": "value", "type": "str"},
        },
    },
    {
        "fhir_path": "encounter.display",
        "columns": {
            "encounter_display": {
                "fhir_key": "encounter.display",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "valueQuantity",
        "columns": {
            "value_quantity_value": {"fhir_key": "value", "type": "str"},
            "value_quantity_unit": {"fhir_key": "unit", "type": "str"},
            "value_quantity_code": {"fhir_key": "code", "type": "str"},
            "value_quantity_system": {"fhir_key": "system", "type": "str"},
        },
    },
    {
        "fhir_path": "valueCodeableConcept.text",
        "columns": {
            "value_codeable_concept_text": {
                "fhir_key": "valueCodeableConcept.text",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "valueRange.low",
        "columns": {
            "value_range_low_value": {"fhir_key": "value", "type": "str"},
            "value_range_low_unit": {"fhir_key": "unit", "type": "str"},
        },
    },
    {
        "fhir_path": "valueRange.high",
        "columns": {
            "value_range_high_value": {"fhir_key": "value", "type": "str"},
            "value_range_high_unit": {"fhir_key": "unit", "type": "str"},
        },
    },
    {
        "fhir_path": "valueRatio.numerator",
        "columns": {
            "value_ratio_numerator_value": {"fhir_key": "value", "type": "str"},
            "value_ratio_numerator_unit": {"fhir_key": "unit", "type": "str"},
            "value_ratio_numerator_code": {"fhir_key": "code", "type": "str"},
        },
    },
    {
        "fhir_path": "valueRatio.denominator",
        "columns": {
            "value_ratio_denominator_value": {
                "fhir_key": "value",
                "type": "str",
            },
            "value_ratio_denominator_unit": {"fhir_key": "unit", "type": "str"},
            "value_ratio_denominator_code": {"fhir_key": "code", "type": "str"},
        },
    },
    {
        "fhir_path": "valueString",
        "columns": {"value_string": {"fhir_key": "valueString", "type": "str"}},
    },
    {
        "fhir_path": "valueBoolean",
        "columns": {
            "value_boolean": {"fhir_key": "valueBoolean", "type": "bool"},
        },
    },
    {
        "fhir_path": "valueInteger",
        "columns": {
            "value_integer": {"fhir_key": "valueInteger", "type": "int"}
        },
    },
    {
        "fhir_path": "effectiveDateTime",
        "columns": {
            "effective_datetime": {
                "fhir_key": "effectiveDateTime",
                "type": "datetime",
            }
        },
    },
    {
        "fhir_path": "issued",
        "columns": {"issued": {"fhir_key": "issued", "type": "datetime"}},
    },
    {
        "fhir_path": "effectivePeriod",
        "columns": {
            "effective_period_start": {"fhir_key": "start", "type": "str"},
            "effective_period_end": {"fhir_key": "end", "type": "str"},
        },
    },
    {
        "fhir_path": "specimen",
        "fhir_reference": "specimen_reference",
        "columns": {
            "specimen_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "specimen_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


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
        super().__init__("Observation", None, TRANSFORM_DICT)
