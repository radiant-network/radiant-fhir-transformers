"""
Unit tests for with_string_constants

with_string_constants returns a copy of a ViewDefinition with string constants
set, escaping values so they survive sqlonfhir's plain-text substitution of
``%name`` into FHIRPath expressions.
"""

import copy

import pytest
from sqlonfhir import evaluate

from radiant_fhir_transform_cli.transform.classes.base import with_string_constants


def _view(path: str, constants: list[dict] | None = None) -> dict:
    """A minimal Patient ViewDefinition with one ``value`` column."""
    view: dict = {
        "resource": "Patient",
        "select": [
            {
                "column": [
                    {"name": "id", "path": "id", "type": "string"},
                    {"name": "value", "path": path, "type": "string"},
                ]
            }
        ],
    }
    if constants is not None:
        view["constant"] = constants
    return view


def _patient(*identifiers: tuple[str, str]) -> dict:
    return {
        "resourceType": "Patient",
        "id": "p1",
        "identifier": [{"type": {"text": text}, "value": value} for text, value in identifiers],
    }


IDENTIFIER_PATH = "identifier.where(type.text = %identifier_type).value"


# --- Building the constant list ---------------------------------------------


def test_adds_constant_when_view_has_no_constant_key():
    result = with_string_constants(_view(IDENTIFIER_PATH), {"identifier_type": "MRN"})

    assert result["constant"] == [{"name": "identifier_type", "valueString": "MRN"}]


def test_appends_to_existing_constants_in_order():
    view = _view(IDENTIFIER_PATH, [{"name": "a", "valueString": "x"}])

    result = with_string_constants(view, {"b": "y", "c": "z"})

    assert result["constant"] == [
        {"name": "a", "valueString": "x"},
        {"name": "b", "valueString": "y"},
        {"name": "c", "valueString": "z"},
    ]


def test_replaces_existing_string_constant_in_place():
    view = _view(
        IDENTIFIER_PATH,
        [
            {"name": "before", "valueString": "1"},
            {"name": "identifier_type", "valueString": "EPI"},
            {"name": "after", "valueString": "2"},
        ],
    )

    result = with_string_constants(view, {"identifier_type": "MRN"})

    assert result["constant"] == [
        {"name": "before", "valueString": "1"},
        {"name": "identifier_type", "valueString": "MRN"},
        {"name": "after", "valueString": "2"},
    ]


@pytest.mark.parametrize(
    "existing",
    [
        {"valueInteger": 1},
        {"valueBoolean": True},
        {"valueCode": "abc"},
        {"valueInteger": 1, "valueString": "stale"},
    ],
)
def test_replacing_removes_other_value_keys(existing):
    """A constant must have exactly one value[x]; old ones are removed."""
    view = _view(IDENTIFIER_PATH, [{"name": "identifier_type", **existing}])

    result = with_string_constants(view, {"identifier_type": "MRN"})

    assert result["constant"] == [{"name": "identifier_type", "valueString": "MRN"}]


def test_replacing_keeps_non_value_keys():
    view = _view(
        IDENTIFIER_PATH,
        [{"name": "identifier_type", "valueString": "EPI", "extension": [{"url": "u"}]}],
    )

    result = with_string_constants(view, {"identifier_type": "MRN"})

    assert result["constant"] == [
        {"name": "identifier_type", "valueString": "MRN", "extension": [{"url": "u"}]}
    ]


def test_empty_constants_returns_equivalent_copy():
    view = _view(IDENTIFIER_PATH, [{"name": "a", "valueString": "x"}])

    result = with_string_constants(view, {})

    assert result == view
    assert result is not view


# --- Copy semantics ----------------------------------------------------------


def test_does_not_mutate_input():
    view = _view(IDENTIFIER_PATH, [{"name": "identifier_type", "valueInteger": 1}])
    original = copy.deepcopy(view)

    with_string_constants(view, {"identifier_type": "MRN", "other": "x"})

    assert view == original


def test_does_not_add_constant_key_to_input():
    view = _view(IDENTIFIER_PATH)

    with_string_constants(view, {"identifier_type": "MRN"})

    assert "constant" not in view


def test_result_is_a_deep_copy():
    view = _view(IDENTIFIER_PATH, [{"name": "a", "valueString": "x"}])

    result = with_string_constants(view, {"b": "y"})
    result["select"][0]["column"][0]["path"] = "changed"
    result["constant"][0]["valueString"] = "changed"

    assert view["select"][0]["column"][0]["path"] == "id"
    assert view["constant"][0]["valueString"] == "x"


def test_repeated_calls_are_independent():
    view = _view(IDENTIFIER_PATH)

    mrn = with_string_constants(view, {"identifier_type": "MRN"})
    epi = with_string_constants(view, {"identifier_type": "EPI"})

    assert mrn["constant"] == [{"name": "identifier_type", "valueString": "MRN"}]
    assert epi["constant"] == [{"name": "identifier_type", "valueString": "EPI"}]


def test_can_be_applied_to_its_own_output():
    first = with_string_constants(_view(IDENTIFIER_PATH), {"identifier_type": "EPI"})

    second = with_string_constants(first, {"identifier_type": "MRN"})

    assert second["constant"] == [{"name": "identifier_type", "valueString": "MRN"}]
    assert first["constant"] == [{"name": "identifier_type", "valueString": "EPI"}]


# --- Validation --------------------------------------------------------------


@pytest.mark.parametrize("value", [1, 1.5, True, None, ["MRN"], {"text": "MRN"}])
def test_rejects_non_string_value(value):
    with pytest.raises(TypeError, match="identifier_type"):
        with_string_constants(_view(IDENTIFIER_PATH), {"identifier_type": value})


def test_rejected_value_does_not_mutate_input():
    view = _view(IDENTIFIER_PATH, [{"name": "a", "valueString": "x"}])
    original = copy.deepcopy(view)

    with pytest.raises(TypeError):
        with_string_constants(view, {"a": "ok", "b": 1})  # type: ignore[dict-item]

    assert view == original


# --- End to end with sqlonfhir -----------------------------------------------


@pytest.mark.parametrize(
    "identifier_type",
    [
        "MRN",
        "",
    ],
)
def test_value_matches_resource_exactly_when_evaluated(identifier_type):
    patient = _patient(("decoy", "wrong"), (identifier_type, "right"))
    view = with_string_constants(_view(IDENTIFIER_PATH), {"identifier_type": identifier_type})

    rows = evaluate(resources=[patient], view_definition=view)

    assert rows == [{"id": "p1", "value": "right"}]


def test_multiple_constants_in_one_path():
    patient = {
        "resourceType": "Patient",
        "id": "p1",
        "identifier": [
            {"system": "s1", "type": {"text": "MRN"}, "value": "wrong-system"},
            {"system": "s2", "type": {"text": "MRN"}, "value": "right"},
        ],
    }
    path = "identifier.where(type.text = %identifier_type and system = %identifier_system).value"
    view = with_string_constants(_view(path), {"identifier_type": "MRN", "identifier_system": "s2"})

    rows = evaluate(resources=[patient], view_definition=view)

    assert rows == [{"id": "p1", "value": "right"}]


def test_constant_in_for_each():
    patient = _patient(("EPI", "epi-1"), ("MRN", "mrn-1"), ("MRN", "mrn-2"))
    view = {
        "resource": "Patient",
        "select": [
            {"column": [{"name": "id", "path": "id", "type": "string"}]},
            {
                "forEach": "identifier.where(type.text = %identifier_type)",
                "column": [{"name": "value", "path": "value", "type": "string"}],
            },
        ],
    }

    rows = evaluate(
        resources=[patient],
        view_definition=with_string_constants(view, {"identifier_type": "MRN"}),
    )

    assert rows == [{"id": "p1", "value": "mrn-1"}, {"id": "p1", "value": "mrn-2"}]
