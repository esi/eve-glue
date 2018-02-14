"""EVE-glue enum utility module."""


import enum


def new_from_enum(name: str, existing: enum.Enum, replace: dict = None,
                  remove: list = None, add: dict = None) -> (enum.Enum):
    """Create a new enum from an existing enum.

    Args:
        name: string name of the new enum
        existing: an existing enum to base from
        replace: dictionary of {name: value} of members to replace
        remove: list of member keys to remove
        add: dictionary of {name: value} of members to add

    Returns:
        a copy of the existing enum, with modifications
    """

    remove = remove or []
    replace = replace or {}

    additions = []
    names = [x.name for x in existing]
    for key, value in (add or {}).items():
        if key in names:
            replace[key] = value
        else:
            additions.append((key, value))

    return enum.Enum(
        name,
        [
            (k.name, replace[k.name] if k.name in replace else k.value)
            for k in existing if k.name not in remove
        ] + additions
    )
