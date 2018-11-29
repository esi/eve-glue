"""Helpers for player owned customs offices (poco)."""
import enum
from eve_glue.enums import new_from_enum


class StructureStateEnumV1(enum.Enum):
    """Enum for poco states."""

    unknown = 0
    unanchored = 1
    anchoring = 2
    online_deprecated = 100  # This only applies to legacy POCOs
    fitting_invulnerable = 101  # This only applies to legacy POCOs
    onlining_vulnerable = 102
    shield_vulnerable = 110
    armor_reinforce = 111
    armor_vulnerable = 112
    hull_reinforce = 113
    hull_vulnerable = 114
    anchor_vulnerable = 115


StructureStateEnumV2 = new_from_enum(  # pylint: disable=invalid-name
    "StructureStateEnumV2",
    StructureStateEnumV1,
    add={
        "deploy_vulnerable": 116
    }
)
