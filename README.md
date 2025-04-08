# 🔥 Transform FHIR JSON to CSV

This repository contains Python classes which use the
[fhirpath-py](https://github.com/beda-software/fhirpath-py) library to
transform FHIR JSON into CSV rows.

A developer writes [FHIR Path expressions](https://www.hl7.org/fhir/fhirpath.html)
to extract the value of a field from the JSON object. 

## 🏁 Quick Start

### Define a Transformer

Define a transformer class in: `radiant_fhir_transform_cli/transform/classes`

This should fairly simple, as the only real implementation is the
transform dictionary `transform_dict`:

```python

TRANSFORM_DICT = {
    "given_name": "name.where(use='official').given.first()",
    "family_name": "name.where(use='official').family",
    "active": "active",
    "birth_date": "birthDate",
    "gender": "gender",
}


class PatientTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Patient", TRANSFORM_DICT)
```

### FHIR Path

The values in the transform dictionary should be strings containing valid 
FHIR path expressions. These expressions provide a way to extract the value 
of a particular field in the FHIR JSON.

The keys of the transform dictionary should be strings containing the 
names of columns in a CSV file.

It is often helpful to use the web site [fhirpath.js](https://hl7.github.io/fhirpath.js/)
while you are writing FHIR path expressions to test them out in real time.

### Test Transformer

You can quickly test your transformer against data by running the following 
CLI command.

```shell
$ radiant fhir transform --resource-type Patient --input-filepath=patient.json
```

If your `patient.json` file looked something like this:

```
{
    "resourceType": "Patient",
    "id": "eNuTIJvJoX5g5enjtR.Ul4ASEfAlFvJjiahhGyW1xd8x43",
    "active": True,
    "name": [
        {
            "use": "official",
            "text": "Testing Careeverywhere",
            "family": "Wong",
            "given": ["Jason"],
        },
        {
            "use": "usual",
            "text": "Testing Careeverywhere",
            "family": "Wong",
            "given": ["Jason Sr"],
        },
    ],
    "gender": "Male",
    "birthDate": "2019-10-17",
    ...
}
```

Your CSV file should show something like:

| given_name | family_name | active | birth_date | gender |
------------ | ----------- | ------ | ---------- | ------ |
Jason        | Wong        | True   | 2019-10-17 | Male   |

## 👩‍💻 Developer Guide

The [developer guide](docs/developer-guide.md) is for individuals that want to
modify existing transformers or add new ones. This guide will provide all
of the information necessary to make changes to the CLI code, and tests.
