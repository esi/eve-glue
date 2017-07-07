from eve_glue import JournalRefTypeEnumV2
from eve_glue import populate_extra_info


def test_journal_ref_type_enum():
    assert JournalRefTypeEnumV2(1).name == "player_trading"
    assert JournalRefTypeEnumV2(17).name == "bounty_prize"


def test_extra_info():
    assert populate_extra_info(1, "test", 123) == \
        {"location_id": 123}
    assert populate_extra_info(1, None, None) == {}

    assert populate_extra_info(233, "abc", 123) == \
        {"argument_name": "abc", "argument_value": 123}
