# 👨🏻‍💻 Developer Guide 

## 🛠️ Setup Dev Environment

### Install Python

This project has been tested with Python 3.12.* Since there are many versions
of Python being used for various projects in D3b, it is a good idea to use
[pyenv](https://realpython.com/intro-to-pyenv/) to manage python versions and
virtual environments.

Follow the [installation instructions here](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)
to install pyenv.

Next install python using pyenv:

```shell
# install latest version of python 3.12
$ pyenv install -v 3.12
```

### Get Source Code

Time to get the source code, install the CLI as an editable Python
package, and install all of the necessary Python dependencies.

```shell
git clone git@github.com:radiant-network/radiant-fhir-transformers.git
cd radiant-fhir-transformers
```

### Setup virtualenv

Next we need to create an isolated environment for our dependencies. For this
we will use pyenv to create a virtualenv with the right version Python.

```shell
# create virtualenv using python 3.12
$ pyenv install 3.12
$ pyenv virtualenv 3.12 fhir-transformer-venv
```

```shell
# Activate the virtualenv
$ pyenv local fhir-transformer-venv
```

```shell
# Install required run dependencies
$ pip install -e .

# Install development and testing dependencies
$ pip install -e .[dev]
$ pip install -e '.[dev]' (if using zsh)
```

### Test Installation

Test that everything installed correctly by running the CLI help:

```shell
radiant --help
```

## ✏️  Define a FHIR Transformer

Define a transformer class in: `radiant_fhir_transform_cli/transform/classes`
Take a look at the [PatientTransformer](radiant_fhir_transform_cli/transform/classes/patient.py)
as an example.

### Note on FHIR Path

The values in the transform dictionary should be strings containing valid 
FHIR path expressions. These expressions provide a way to extract the value 
of a particular field in the FHIR JSON.

The keys of the transform dictionary should be strings containing the 
names of columns in a CSV file.

It is often helpful to use the web site [fhirpath.js](https://hl7.github.io/fhirpath.js/)
while you are writing FHIR path expressions to test them out in real time.

### Patient Transformer
The example below shows the `PatientTransformer` which has already 
been implemented:

```python
# radiant_fhir_transform_cli/transform/classes/patient.py

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

### Add to Imports

Once you've defined a transformer class, remember to add it to the list 
of transformers here:

```python
# radiant_fhir_transform_cli/transform/classes/__init__.py

from radiant_fhir_transform_cli.transform.classes.patient import (
    PatientTransformer
)

# Map FHIR resource type to its transformer class
transformers = {"Patient": PatientTransformer}

```

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

Your output CSV file should show something like:

| given_name | family_name | active | birth_date | gender |
------------ | ----------- | ------ | ---------- | ------ |
Jason        | Wong        | True   | 2019-10-17 | Male   |

## ✅ Unit Tests

Every transformer class should have a unit test. Luckily the structure of the 
unit tests is setup so that the developer only has to implement a "test helper"
class. 

The test helper class defines an example FHIR payload and an expected output 
that will be supplied to the unit tests to ensure that the transformer 
yielded an output that matches the expected output. 

Here is an example for the `PatientTestHelper`:

```python

# tests/data/patient.py

from tests.data.base import FhirResourceTestHelper

RESOURCE = {
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

EXPECTED_OUTPUT = {
    "given_name": "Testing",
    "family_name": "Careeverywhere",
    "birth_date": "2005-02-27",
    "active": True,
    "gender": "Female",
}


class PatientTestHelper(FhirResourceTestHelper):

    resource_type = "Patient"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

```

### Add to Unit Tests 

Once the test helper has been implemented, it needs to be added to the 
list of test helpers that will be run in the unit tests:

```python 

# tests/data/__init__.py

from tests.data.patient import PatientTestHelper


test_helpers = {
    PatientTestHelper.resource_type: PatientTestHelper
}

```

### Run Tests 
Tests are run using pytest

```shell
$ pytest tests/unit
```

## 🚨 Code Format and Style

To maintain code consistency and readability across our project, we use
[black](https://black.readthedocs.io/en/stable/), a popular Python code formatter.
The formatter ensures that all Python files in our repository adhere to a uniform style,
minimizing the need for code style discussions during code reviews.

### Run Linter

We run the linter on the `radiant_fhir_transform_cli` and the `tests` folders.

```bash
$black --line-length 80 radiant_fhir_transform_cli tests
```

You should see something like the following.

```text
All done! ✨ 🍰 ✨
2 files reformatted, 170 files left unchanged.
```
