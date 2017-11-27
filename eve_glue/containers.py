"""Helpers for audit log secure containers."""


import enum


class ActionsEnumV1(enum.Enum):
    """Maps ALSC Actions to IDs. Taken from the invALSCActions db table."""

    assemble = 1
    repackage = 2
    set_name = 3
    move = 4
    set_password = 5
    add = 6
    lock = 7
    unlock = 8
    enter_password = 9
    configure = 10


class PasswordTypeEnumV1(enum.Enum):
    """Maps ALSC password types to IDs."""

    general = 1
    config = 2
