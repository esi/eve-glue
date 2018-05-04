"""Helpers for faction warfare concepts."""

import enum


class SystemContestationState(enum.Enum):
    """The contested states for systems in faction warfare."""

    uncontested = 0
    contested = 1
    vulnerable = 2
    captured = 3
