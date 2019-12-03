"""Helpers for resolving the location type by ID."""


def resolve_location_type_enum(location_id):
    """Resolve the location itemID ID to a type name."""

    if 30000000 <= location_id <= 39999999:
        return "solar_system"
    if 60000000 <= location_id < 64000000:
        return "station"
    if location_id >= 100000000:
        return "item"

    return "other"
