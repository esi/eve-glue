"""Helpers for evaluating standing."""


def read_standing_from_proto(standing_proto):
    """Convert protobuf standing value message to float."""

    return standing_proto.units + (standing_proto.nanos * (10**-9))
