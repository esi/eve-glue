from eve_glue import resolve_journal_ref_type_enum
from eve_glue import populate_extra_info


def test_resolve_journal_ref_type():
    assert resolve_journal_ref_type_enum(1) == "player_trading"
    assert resolve_journal_ref_type_enum(233) == "unknown"


def test_extra_info():
    assert populate_extra_info(1, "test", 123) == \
        {"location_name": "test", "location_id": 123}
    assert populate_extra_info(1, None, None) == {}

    assert populate_extra_info(233, "abc", 123) == \
        {"argument_name": "abc", "argument_value": 123}
