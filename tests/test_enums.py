"""Pytests for the eve_glue module enums."""


import enum

import pytest

from eve_glue import enums


def test_new_from_enum():
    """Ensure basic functionality."""

    class A(enum.Enum):
        Thing = "Stuff"
        Other = "Thing"

    B = enums.new_from_enum(
        "B",
        A,
        remove=["Other"],
        add={"Thing": "Changed", "foo": "bar"},
    )

    with pytest.raises(AttributeError):
        B.Other

    assert B.Thing.value == "Changed"
    assert B.foo.value == "bar"
