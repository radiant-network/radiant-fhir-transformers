"""
Transformer config

A single, optional config dict that can be passed to any transformer. Every key
is optional; a transformer reads only the section it cares about and falls back
to its defaults for anything missing.

    config: FhirTransformerConfigTypeDef = {"patient": {"identifier_type": "MRN"}}
    transformer = PatientTransformer(config)

Config may change the *values* a transformer extracts, never its schema
(column names and types).
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, NotRequired, TypedDict, get_type_hints, is_typeddict


class FhirTransformerConfigTypeDef(TypedDict):
    patient: NotRequired[PatientTransformerConfigTypeDef]


class PatientTransformerConfigTypeDef(TypedDict):
    # Identifier.type.text of the identifier to emit as patient.identifier_mrn
    identifier_type: NotRequired[str]


def validate_config(
    config: Mapping[str, Any],
    type_def: type = FhirTransformerConfigTypeDef,
    _path: str = "config",
) -> None:
    """Validate a config dict against its TypedDict definition at runtime.

    TypedDicts are only checked statically, so a misspelled key would otherwise
    be silently ignored and the transformer would fall back to its default.

    Args:
        config: The config dict (or section) to validate.
        type_def: The TypedDict the config must conform to.

    Raises:
        TypeError: If the config or one of its values has the wrong type.
        ValueError: If the config has a key the TypedDict does not define.
    """
    if not isinstance(config, Mapping):
        raise TypeError(f"{_path} must be a dict, got {type(config).__name__}")

    hints = get_type_hints(type_def)

    unknown = sorted(set(config) - set(hints))
    if unknown:
        raise ValueError(f"Unknown key(s) in {_path}: {unknown}. Valid keys: {sorted(hints)}")

    for key, value in config.items():
        expected = hints[key]
        key_path = f"{_path}[{key!r}]"
        if is_typeddict(expected):
            validate_config(value, expected, key_path)
        elif isinstance(expected, type) and not isinstance(value, expected):
            raise TypeError(f"{key_path} must be {expected.__name__}, got {type(value).__name__}")
