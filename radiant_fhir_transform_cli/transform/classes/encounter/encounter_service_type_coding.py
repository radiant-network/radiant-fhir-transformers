""" 
Fhir Encounter Service Type Coding Class
"""

from radiant_fhir_transform_cli.transform.classes.base import FhirResourceTransformer

TRANSFORM_SCHEMA = [
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
            "encounter_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "serviceType.coding",
        "columns": {
            "service_type_coding_system": {"fhir_key": "system", "type": "str"},
            "service_type_coding_code": {"fhir_key": "code", "type": "str"},
            "service_type_coding_display": {"fhir_key": "display", "type": "str"},
        },
    },
]

class EncounterServiceTypeCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Encounter' resource in FHIR, focusing on the 'serviceType.coding' element.

    This class transforms FHIR Encounter JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'serviceType.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Encounter').
        subtype (str): Specifies the sub-element of the resource to focus on ('service_type_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.
    """

    def __init__(self):
        super().__init__("Encounter", "service_type_coding", TRANSFORM_SCHEMA)