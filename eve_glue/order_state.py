ORDER_STATE_TO_ENUM = {
    0: "open",
    1: "closed",
    2: "expired",
    3: "cancelled",
    4: "pending",
    5: "character_deleted"
}

ORDER_STATE_DICT = { v:k for k,v in ORDER_STATE_TO_ENUM.items()}
