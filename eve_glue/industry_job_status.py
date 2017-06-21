JOB_STATUS_TO_ENUM = {
    1: "active",
    2: "paused",
    3: "ready",
    101: "delivered",
    102: "cancelled",
    103: "reverted"
}


def resolve_industry_job_status_enum(status_id):
    """
    status:
        type: string
        enum:
            - active
            - paused
            - ready
            - delivered
            - cancelled
            - reverted
    """
    return JOB_STATUS_TO_ENUM[status_id]
