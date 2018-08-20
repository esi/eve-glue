"""Helpers for resolving the location type by ID."""


def resolve_location_type_enum(location_type_id):
    """Resolve the location type ID to name."""

    if 30000000 <= location_type_id <= 39999999:
        return "solar_system"
    if 60000000 <= location_type_id < 64000000:
        return "station"
    return "other"
