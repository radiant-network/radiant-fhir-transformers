import json
import hashlib
from typing import Any, Tuple, override

from collections import defaultdict

from .base import FhirResourceTransformer

VIEW_DEFINITION = {
    "resourceType": "ViewDefinition",
    "resource": None,
    "constant": [
        {
            "name": "org_short_code",
            "valueString": "",
        },
        {
            "name": "registry_short_code",
            "valueString": "",
        },
        {
            "name": "last_processed",
            "valueString": "",
        },
        {
            "name": "size_bytes",
            "valueString": "",
        },
        {
            "name": "hash_md5",
            "valueString": "",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "id",
                },
                {
                    "name": "last_processed",
                    "path": "%last_processed",
                },
                {
                    "name": "resource_type",
                    "path": "resourceType",
                },
                {
                    "name": "org_short_code",
                    "path": "%org_short_code",
                },
                {
                    "name": "registry_short_code",
                    "path": "%registry_short_code",
                },
                {
                    "name": "size_bytes",
                    "path": "%size_bytes",
                },
                {
                    "name": "hash_md5",
                    "path": "%hash_md5",
                },
                {
                    "name": "json",
                    "path": "$this",
                },
            ],
        },
    ],
}


class RawFhirResourceTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("fhir_resource", None, VIEW_DEFINITION)

    def _compute_payload_hash_and_size(
        self, resource: dict[str, Any]
    ) -> Tuple[str, int]:
        """
        Compute both the MD5 hash and the byte size of the FHIR
        resource payload.

        The resource is serialized into a canonical JSON form:
        - Keys are sorted for deterministic output.
        - Whitespace is minimized (compact separators).
        Both the hash and size are computed from the same byte string to
        ensure consistency.

        Args:
            resource: The FHIR resource as a Python dictionary.

        Returns:
            A tuple of:
                (payload_hash: str, payload_size_bytes: int)
        """
        # Canonical JSON serialization
        payload_str = json.dumps(
            resource, sort_keys=True, separators=(",", ":")
        )
        payload_bytes = payload_str.encode("utf-8")

        # Compute SHA-256 hash
        payload_hash = hashlib.md5(payload_bytes).hexdigest()

        # Compute size in bytes
        payload_size = len(payload_bytes)

        return payload_hash, payload_size

    @override
    def transform_resources(
        self, resources: list[dict]
    ) -> list[dict[str, Any]]:
        resources_by_type = defaultdict(list)
        for resource in resources:
            resources_by_type[resource["resourceType"]].append(resource)

        output = []
        for resource_type, resource_list in resources_by_type.items():
            self.view_definition["resource"] = resource_type
            output.extend(super().transform_resources(resource_list))

        updated_rows = []
        for row in output:
            hash_value, size_bytes = self._compute_payload_hash_and_size(
                row["json"]
            )
            row["hash_md5"] = hash_value
            row["size_bytes"] = str(size_bytes)
            updated_rows.append(row)

        return updated_rows
