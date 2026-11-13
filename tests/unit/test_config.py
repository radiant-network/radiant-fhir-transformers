"""
Unit tests for transformer config
"""

import copy

import pytest

from radiant_fhir_transform_cli.transform.classes import transformers
from radiant_fhir_transform_cli.transform.classes.base import FhirResourceTransformer
from radiant_fhir_transform_cli.transform.classes.fhir_resource_config import (
    FhirTransformerConfigTypeDef,
    validate_config,
)
from radiant_fhir_transform_cli.transform.classes.patient.patient import (
    VIEW_DEFINITION,
    PatientTransformer,
)
from radiant_fhir_transform_cli.transform.classes.raw_fhir import (
    RawFhirResourceTransformer,
)

PATIENT = {
    "resourceType": "Patient",
    "id": "p1",
    "gender": "female",
    "identifier": [
        {"type": {"text": "EPI"}, "value": "epi-1"},
        {"type": {"text": "MRN"}, "value": "mrn-1"},
        {"type": {"text": "SCHMRN"}, "value": "odd-1"},
    ],
}

ALL_TRANSFORMERS = [cls for classes in transformers.values() for cls in classes] + [
    RawFhirResourceTransformer
]


def _mrn(transformer: PatientTransformer) -> str | None:
    return transformer.transform_resources([copy.deepcopy(PATIENT)])[0]["identifier_mrn"]


@pytest.mark.parametrize("config", [None, {}, {"patient": {}}])
def test_patient_identifier_type_default(config):
    assert _mrn(PatientTransformer(config)) == "epi-1"


@pytest.mark.parametrize(
    "identifier_type,expected",
    [("MRN", "mrn-1"), ("SCHMRN", "odd-1"), ("missing", None)],
)
def test_patient_identifier_type_from_config(identifier_type, expected):
    config: FhirTransformerConfigTypeDef = {"patient": {"identifier_type": identifier_type}}
    assert _mrn(PatientTransformer(config)) == expected


def test_config_does_not_leak_between_instances():
    original = copy.deepcopy(VIEW_DEFINITION)
    configured = PatientTransformer({"patient": {"identifier_type": "MRN"}})

    assert VIEW_DEFINITION == original
    assert _mrn(PatientTransformer()) == "epi-1"
    assert _mrn(configured) == "mrn-1"


def test_config_does_not_change_schema():
    configured = PatientTransformer({"patient": {"identifier_type": "MRN"}})
    assert configured.column_metadata() == PatientTransformer().column_metadata()


@pytest.mark.parametrize("cls", ALL_TRANSFORMERS)
def test_every_transformer_accepts_config(cls):
    config: FhirTransformerConfigTypeDef = {"patient": {"identifier_type": "MRN"}}
    transformer = cls(config)

    assert transformer.config == config
    # each instance owns its view definition; the class-level one is a template
    assert transformer.view_definition is not cls.view_definition


@pytest.mark.parametrize(
    "config,error",
    [
        ({"pateint": {}}, ValueError),
        ({"patient": {"identifer_type": "MRN"}}, ValueError),
        ({"patient": {"identifier_type": 1}}, TypeError),
        ({"patient": "MRN"}, TypeError),
        ("MRN", TypeError),
    ],
)
def test_invalid_config_is_rejected(config, error):
    with pytest.raises(error):
        validate_config(config)
    with pytest.raises(error):
        PatientTransformer(config)


def test_transformer_without_class_attributes_is_rejected():
    with pytest.raises(TypeError):
        FhirResourceTransformer()
