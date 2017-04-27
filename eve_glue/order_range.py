ORDER_RANGE_TO_ENUM = {
    32767: "region",
    -1: "station",
    0: "solarsystem",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    10: "10",
    20: "20",
    30: "30",
    40: "40"
}

def resolve_order_range_enum(order_state_id):
    """
    range:
        type: string
        description: Valid order range, numbers are ranges in jumps
        enum:
            - station
            - region
            - solarsystem
            - "1"
            - "2"
            - "3"
            - "4"
            - "5"
            - "10"
            - "20"
            - "30"
            - "40"
    """
    return ORDER_RANGE_TO_ENUM[order_state_id]
