"""Pytests for the eve_glue module enums."""


import enum

import pytest

from eve_glue import enums


def test_new_from_enum():
    """Ensure basic functionality."""

    class A(enum.Enum):
        Thing = "Stuff"
        Other = "Thing"
        AddReplace = True

    B = enums.new_from_enum(
        "B",
        A,
        replace={"Thing": "Changed"},
        remove=["Other"],
        add={"foo": "bar", "AddReplace": False},
    )

    with pytest.raises(AttributeError):
        B.Other

    assert B.Thing.value == "Changed"
    assert B.foo.value == "bar"
    assert B.AddReplace.value is False
