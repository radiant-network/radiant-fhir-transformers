# 🔥 Transform FHIR JSON to CSV

Welcome to the **Radiant FHIR Transformers** repository. This project provides a scalable,
standards-based Python pipeline for transforming raw, nested FHIR NDJSON into flat, tabular
datasets (CSV) ready for analytics and machine learning workloads.

## 🏗️ Architecture: SQL on FHIR (v2)

This repository has been upgraded to implement the official **SQL on FHIR v2** standard. We no
longer use custom Python dictionaries to define transformations. Instead, we use standard
`ViewDefinition` JSON artifacts and evaluate them using the
[SAS `sqlonfhir` Python engine](https://github.com/sassoftware/sqlonfhir).

This architectural shift ensures:
1. **Portability:** Our transformation schemas (`ViewDefinitions`) are decoupled from our Python
code. They can be shared, versioned, and executed by any compliant runner.

2. **Standardization:** We use official HL7 FHIRPath for extraction, unnesting arrays (`forEach`),
and conditional filtering (`where`).

3. **Pipeline Readiness:** The in-memory Python runner natively outputs flat dictionaries, making
it trivial to convert to Pandas DataFrames or PySpark DataFrames for downstream processing in AWS
(e.g., writing to S3 via EMR for Athena querying).

## 🏁 Quick Start

### 1. Installation

Ensure you have a modern Python environment (we recommend managing dependencies via Docker for consistency).

```bash
# Install Radiant CLI tools
pip install -e .
```

### 2. Define a ViewDefinition

Transformations are now defined as strictly typed `ViewDefinition` JSON objects. Create a new
definition (e.g., `views/PatientDemographics.json`):

```json
{
  "resource": "Patient",
  "name": "radiant_patient_demographics",
  "select": [
    {
      "column": [
        {"name": "patient_id", "path": "id"},
        {"name": "active", "path": "active"},
        {"name": "birth_date", "path": "birthDate"},
        {"name": "gender", "path": "gender"}
      ]
    },
    {
      "forEach": "name.where(use='official').first()",
      "column": [
        {"name": "given_name", "path": "given.join(' ')"},
        {"name": "family_name", "path": "family"}
      ]
    }
  ]
}
```

### 3. Run the Transformer

You can test your view against a sample FHIR NDJSON file using the Radiant CLI. The CLI leverages
the `sqlonfhir.evaluate()` function under the hood.

```bash
$ radiant fhir transform \
    --view=views/PatientDemographics.json \
    --input=patient.ndjson \
    --output=output.csv
```

## 👩‍💻 Developer Guide

The [developer guide](docs/developer-guide.md)  is for individuals that want to modify existing
transformers or add new ones. This guide will provide all of the information necessary to make
changes to the CLI code, and tests.

