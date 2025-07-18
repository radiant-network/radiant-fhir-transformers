"""
FHIR Observation EffectiveTiming Repeat DayOfWeek transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
    {
        "fhir_path": None,
        "columns": {
            "id": {"fhir_key": None, "type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "observation_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "effectiveTiming.repeat.dayOfWeek",
        "columns": {
            "effective_timing_repeat_day_of_week": {
                "fhir_key": "dayOfWeek",
                "type": "str",
            },
        },
    },
]


class ObservationEffectiveTimingRepeatDayOfWeekTransformer(
    FhirResourceTransformer
):
    """
    Transformer class for the 'Observation' resource in FHIR, focusing on the 'effectiveTiming.repeat.dayOfWeek' element.

    This class transforms FHIR Observation JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'effectiveTiming.repeat.dayOfWeek' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Observation').
        subtype (str): Specifies the sub-element of the resource to focus on ('effective_timing_repeat_day_of_week').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ObservationEffectiveTimingRepeatDayOfWeekTransformer instance with the resource type 'Observation',
            subtype 'effective_timing_repeat_day_of_week', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "Observation",
            "effective_timing_repeat_day_of_week",
            TRANSFORM_SCHEMA,
        )
