import enum


class ActionsEnumV1(enum.Enum):
    """Maps ALSC Actions to IDs. Taken from the invALSCActions db table."""

    Assemble = 1
    Repackage = 2
    SetName = 3
    Move = 4
    SetPassword = 5
    Add = 6
    Lock = 7
    Unlock = 8
    EnterPassword = 9
    Configure = 10


class PasswordTypeEnumV1(enum.Enum):
    """Maps ALSC password types to IDs."""

    General = 1
    Config = 2
