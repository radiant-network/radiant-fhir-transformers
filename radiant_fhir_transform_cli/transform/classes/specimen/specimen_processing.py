"""
FHIR Specimen Processing transformer
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
            "specimen_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "processing",
        "columns": {
            "processing_description": {"fhir_key": "description", "type": "str"},
            "processing_procedure_coding": {"fhir_key": "procedure.coding", "type": "str"},
            "processing_procedure_text": {"fhir_key": "procedure.text", "type": "str"}, 
            "processing_additive": {"fhir_key": "additive", "type": "str"},
            "processing_time_date_time": {"fhir_key": "timeDateTime", "type": "datetime"},
            "processing_time_period_start": {"fhir_key": "timePeriod.start", "type": "datetime"},
            "processing_time_period_end": {"fhir_key": "timePeriod.end", "type": "datetime"},           
        },
    },
]


class SpecimenProcessingTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'Specimen' resource in FHIR, focusing on the 'processing' element.

    This class transforms FHIR Specimen JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'processing' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Specimen').
        subtype (str): Specifies the sub-element of the resource to focus on ('processing').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the SpecimenProcessing instance with the resource type 'Specimen',
            subtype 'processing', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Specimen", "processing", TRANSFORM_SCHEMA)
