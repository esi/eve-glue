"""Pytests for the eve_glue module standing."""

from eve_glue import standing
from eve.standing.standing_pb2 import Value as StandingValue


def test_read_standing_from_proto():
    """Test read standing from proto."""

    assert standing.read_standing_from_proto(
        StandingValue(units=2, nanos=232543000)) == 2.232543
    assert standing.read_standing_from_proto(
        StandingValue(units=-2, nanos=-131200000)) == -2.1312
    assert standing.read_standing_from_proto(
        StandingValue(units=0, nanos=-131200000)) == -0.1312
    assert standing.read_standing_from_proto(
        StandingValue(units=0, nanos=131200000)) == 0.1312
    assert standing.read_standing_from_proto(StandingValue(units=0,
                                                           nanos=0)) == 0
