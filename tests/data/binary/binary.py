"""
Test helper class for FHIR resource type Binary
"""

from radiant_fhir_transform_cli.transform.classes.binary import (
    BinaryTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .binary_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "resource_type": "Binary",
        "id": "example",
        "content_type": "text/html",
        "security_context_reference": None,
        "security_context_type": None,
        "security_context_display": None,
        "data": "PCFET0NUWVBFIGh0bWw+CjxodG1sPgo8aGVhZD4KICA8bWV0YSBjaGFyc2V0PVwiVVRGLThcIj4KICA8dGl0bGU+UGF0aG9sb2d5IFJlcG9ydDwvdGl0bGU+CiAgPHN0eWxlPgogICAgYm9keSB7IGZvbnQtZmFtaWx5OiBBcmlhbCwgc2Fucy1zZXJpZjsgbWFyZ2luOiA0MHB4OyB9CiAgICBoMSwgaDIgeyBjb2xvcjogIzJGNEM0RjsgfQogICAgdGFibGUgeyBib3JkZXItY29sbGFwc2U6IGNvbGxhcHNlOyB3aWR0aDogMTAwJTsgbWFyZ2luLXRvcDogMjBweDsgfQogICAgdGgsIHRkIHsgYm9yZGVyOiAxcHggc29saWQgI2NjYzsgcGFkZGluZzogOHB4OyB0ZXh0LWFsaWduOiBsZWZ0OyB9CiAgICB0aCB7IGJhY2tncm91bmQtY29sb3I6ICNmMGYwZjA7IH0KICA8L3N0eWxlPgo8L2hlYWQ+Cjxib2R5PgoKICA8aDE+UGF0aG9sb2d5IFJlcG9ydDwvaDE+CgogIDxwPjxzdHJvbmc+UGF0aWVudCBOYW1lOjwvc3Ryb25nPiBKb2huIERvZTwvcD4KICA8cD48c3Ryb25nPk1lZGljYWwgUmVjb3JkIE51bWJlcjo8L3N0cm9uZz4gMTIzNDU2Nzg8L3A+CiAgPHA+PHN0cm9uZz5EYXRlIG9mIEJpcnRoOjwvc3Ryb25nPiAxOTgwLTA0LTE1PC9wPgogIDxwPjxzdHJvbmc+UmVwb3J0IERhdGU6PC9zdHJvbmc+IDIwMjUtMDgtMDY8L3A+CiAgPHA+PHN0cm9uZz5SZWZlcnJpbmcgUGh5c2ljaWFuOjwvc3Ryb25nPiBEci4gRW1pbHkgQ2FydGVyPC9wPgoKICA8aHI+CgogIDxoMj5TcGVjaW1lbiBJbmZvcm1hdGlvbjwvaDI+CiAgPHA+PHN0cm9uZz5TcGVjaW1lbiBJRDo8L3N0cm9uZz4gUy0yMDI1MDgwNi0wMDE8L3A+CiAgPHA+PHN0cm9uZz5TcGVjaW1lbiBUeXBlOjwvc3Ryb25nPiBMZWZ0IEJyZWFzdCBUaXNzdWUgQmlvcHN5PC9wPgogIDxwPjxzdHJvbmc+RGF0ZSBDb2xsZWN0ZWQ6PC9zdHJvbmc+IDIwMjUtMDgtMDM8L3A+CiAgPHA+PHN0cm9uZz5SZWNlaXZlZDo8L3N0cm9uZz4gMjAyNS0wOC0wNDwvcD4KCiAgPGhyPgoKICA8aDI+RGlhZ25vc2lzPC9oMj4KICA8cD4KICAgIEludmFzaXZlIGR1Y3RhbCBjYXJjaW5vbWEsIEdyYWRlIElJIChtb2RlcmF0ZWx5IGRpZmZlcmVudGlhdGVkKS4gVHVtb3Igc2l6ZSBhcHByb3hpbWF0ZWx5IDEuOCBjbS4KICA8L3A+CiAgPHA+CiAgICBNYXJnaW5zIGFyZSBuZWdhdGl2ZSBmb3IgdHVtb3IgaW52b2x2ZW1lbnQuIEx5bXBob3Zhc2N1bGFyIGludmFzaW9uIGlzIG5vdCBpZGVudGlmaWVkLgogIDwvcD4KCiAgPGgyPkltbXVub2hpc3RvY2hlbWlzdHJ5PC9oMj4KICA8dGFibGU+CiAgICA8dGhlYWQ+CiAgICAgIDx0cj4KICAgICAgICA8dGg+TWFya2VyPC90aD4KICAgICAgICA8dGg+U3RhdHVzPC90aD4KICAgICAgICA8dGg+SW50ZXJwcmV0YXRpb248L3RoPgogICAgICA8L3RyPgogICAgPC90aGVhZD4KICAgIDx0Ym9keT4KICAgICAgPHRyPgogICAgICAgIDx0ZD5Fc3Ryb2dlbiBSZWNlcHRvciAoRVIpPC90ZD4KICAgICAgICA8dGQ+UG9zaXRpdmU8L3RkPgogICAgICAgIDx0ZD45MCUgb2YgdHVtb3IgY2VsbHMgc2hvdyBzdHJvbmcgbnVjbGVhciBzdGFpbmluZzwvdGQ+CiAgICAgIDwvdHI+CiAgICAgIDx0cj4KICAgICAgICA8dGQ+UHJvZ2VzdGVyb25lIFJlY2VwdG9yIChQUik8L3RkPgogICAgICAgIDx0ZD5Qb3NpdGl2ZTwvdGQ+CiAgICAgICAgPHRkPjc1JSBvZiB0dW1vciBjZWxscyBzaG93IG1vZGVyYXRlIG51Y2xlYXIgc3RhaW5pbmc8L3RkPgogICAgICA8L3RyPgogICAgICA8dHI+CiAgICAgICAgPHRkPkhFUjIvbmV1PC90ZD4KICAgICAgICA8dGQ+TmVnYXRpdmUgKFNjb3JlIDErKTwvdGQ+CiAgICAgICAgPHRkPk5vIGFtcGxpZmljYXRpb24gZGV0ZWN0ZWQ8L3RkPgogICAgICA8L3RyPgogICAgICA8dHI+CiAgICAgICAgPHRkPktpLTY3PC90ZD4KICAgICAgICA8dGQ+MjUlPC90ZD4KICAgICAgICA8dGQ+TW9kZXJhdGUgcHJvbGlmZXJhdGl2ZSBpbmRleDwvdGQ+CiAgICAgIDwvdHI+CiAgICA8L3Rib2R5Pgo8L3RhYmxlPgoKICA8aHI+CgogIDxoMj5QYXRob2xvZ2lzdDwvaDI+CiAgPHA+PHN0cm9uZz5OYW1lOjwvc3Ryb25nPiBEci4gU2FtYW50aGEgTGluLCBNRDwvcD4KICA8cD48c3Ryb25nPkxpY2Vuc2U6PC9zdHJvbmc+IFBBIDQ1Mzg5MjwvcD4KICA8cD48c3Ryb25nPlNpZ25lZDo8L3N0cm9uZz4gMjAyNS0wOC0wNiAxNDoyMyBFRFQ8L3A+Cgo8L2JvZHk+CjwvaHRtbD4=",
    }
]


class BinaryTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Binary' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Binary' resource.

    It predefines the resource type as 'Binary'
    and initializes the resource with the specific 'Binary' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Binary'.
        resource (dict): The raw FHIR 'Binary' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'Binary' resource payload.
    """

    resource_type = "Binary"
    resource_subtype = None
    transformer = BinaryTransformer
    expected_table_name = "binary"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
