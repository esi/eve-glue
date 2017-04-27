ORDER_STATE_TO_ENUM = {
    0: "open",
    1: "closed",
    2: "expired",
    3: "cancelled",
    4: "pending",
    5: "character_deleted"
}

def resolve_order_state_enum(order_state_id):
    """
    state:
        type: string
        description: Current order state
        enum:
            - open
            - closed
            - expired
            - cancelled
            - pending
            - character_deleted
    """
    return ORDER_STATE_TO_ENUM[order_state_id]
