"""Helpers for resolving the location type by ID."""


def resolve_location_type_enum(location_type_id):
    """Resolve the location type ID to name."""

    if location_type_id <= 10000:
        return "solar_system"
    if (location_type_id >= 60000000) and (location_type_id < 64000000):
        return "station"
    return "other"
