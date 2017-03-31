def resolve_location_type_enum(location_type_id):
    if location_id <= 10000:
        return "solar_system"
    if (location_id >= 60000000) and (location_id < 64000000):
        return "station"
    return "other"
