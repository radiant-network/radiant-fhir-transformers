"""
Unit tests for FhirResourceTransformer.__init_subclass__

Subclasses must define (or inherit) the class attributes ``resource_type`` and
``view_definition``. An incomplete subclass fails when the class is defined
(i.e. at import time), not when it is first instantiated.
"""

import pytest

from radiant_fhir_transform_cli.transform.classes import transformers
from radiant_fhir_transform_cli.transform.classes.base import FhirResourceTransformer
from radiant_fhir_transform_cli.transform.classes.patient import (
    PatientAddressTransformer,
    PatientTransformer,
)
from radiant_fhir_transform_cli.transform.classes.raw_fhir import (
    RawFhirResourceTransformer,
)

VIEW = {"resource": "Patient", "select": [{"column": [{"name": "id", "path": "id"}]}]}


def test_missing_both_attributes_is_rejected_at_definition():
    with pytest.raises(TypeError) as exc_info:

        class IncompleteTransformer(FhirResourceTransformer):
            pass

    message = str(exc_info.value)
    assert "IncompleteTransformer" in message
    assert "resource_type" in message
    assert "view_definition" in message


def test_missing_resource_type_is_rejected_at_definition():
    with pytest.raises(TypeError, match="NoResourceTypeTransformer") as exc_info:

        class NoResourceTypeTransformer(FhirResourceTransformer):
            view_definition = VIEW

    assert "resource_type" in str(exc_info.value)
    assert "view_definition" not in str(exc_info.value)


def test_missing_view_definition_is_rejected_at_definition():
    with pytest.raises(TypeError, match="NoViewTransformer") as exc_info:

        class NoViewTransformer(FhirResourceTransformer):
            resource_type = "Patient"

    assert "view_definition" in str(exc_info.value)
    assert "resource_type" not in str(exc_info.value)


def test_annotation_alone_does_not_count_as_defined():
    """A bare annotation creates no attribute, so it must still be rejected."""
    with pytest.raises(TypeError, match="view_definition"):

        class AnnotatedOnlyTransformer(FhirResourceTransformer):
            resource_type = "Patient"
            view_definition: dict


def test_complete_subclass_is_accepted_without_resource_component():
    class MinimalTransformer(FhirResourceTransformer):
        resource_type = "Patient"
        view_definition = VIEW

    transformer = MinimalTransformer()

    assert transformer.resource_component is None
    assert transformer.table_name == "patient"


def test_complete_subclass_with_resource_component_is_accepted():
    class ComponentTransformer(FhirResourceTransformer):
        resource_type = "Patient"
        resource_component = "address"
        view_definition = VIEW

    assert ComponentTransformer().table_name == "patient_address"


def test_inherited_attributes_satisfy_the_check():
    class CustomPatientTransformer(PatientTransformer):
        pass

    transformer = CustomPatientTransformer()

    assert transformer.table_name == PatientTransformer().table_name
    assert transformer.column_metadata() == PatientTransformer().column_metadata()


def test_subclass_can_override_inherited_attributes():
    class CustomAddressTransformer(PatientAddressTransformer):
        resource_component = "custom_address"

    assert CustomAddressTransformer().table_name == "patient_custom_address"


@pytest.mark.parametrize(
    "cls",
    [cls for classes in transformers.values() for cls in classes] + [RawFhirResourceTransformer],
    ids=lambda cls: cls.__name__,
)
def test_every_registered_transformer_defines_required_attributes(cls):
    assert isinstance(cls.resource_type, str) and cls.resource_type
    assert isinstance(cls.view_definition, dict) and cls.view_definition
