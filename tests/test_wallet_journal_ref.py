from eve_glue import JournalRefTypeEnumV2
from eve_glue import populate_extra_info


def test_journal_ref_type_enum():
    assert JournalRefTypeEnumV2(1).name
    assert JournalRefTypeEnumV2(2).name
    assert JournalRefTypeEnumV2(3).name
    assert JournalRefTypeEnumV2(9).name
    assert JournalRefTypeEnumV2(10).name
    assert JournalRefTypeEnumV2(11).name
    assert JournalRefTypeEnumV2(12).name
    assert JournalRefTypeEnumV2(13).name
    assert JournalRefTypeEnumV2(15).name
    assert JournalRefTypeEnumV2(16).name
    assert JournalRefTypeEnumV2(17).name
    assert JournalRefTypeEnumV2(19).name
    assert JournalRefTypeEnumV2(26).name
    assert JournalRefTypeEnumV2(27).name
    assert JournalRefTypeEnumV2(30).name
    assert JournalRefTypeEnumV2(31).name
    assert JournalRefTypeEnumV2(33).name
    assert JournalRefTypeEnumV2(34).name
    assert JournalRefTypeEnumV2(35).name
    assert JournalRefTypeEnumV2(37).name
    assert JournalRefTypeEnumV2(38).name
    assert JournalRefTypeEnumV2(39).name
    assert JournalRefTypeEnumV2(40).name
    assert JournalRefTypeEnumV2(41).name
    assert JournalRefTypeEnumV2(42).name
    assert JournalRefTypeEnumV2(46).name
    assert JournalRefTypeEnumV2(48).name
    assert JournalRefTypeEnumV2(49).name
    assert JournalRefTypeEnumV2(50).name
    assert JournalRefTypeEnumV2(51).name
    assert JournalRefTypeEnumV2(52).name
    assert JournalRefTypeEnumV2(54).name
    assert JournalRefTypeEnumV2(55).name
    assert JournalRefTypeEnumV2(56).name
    assert JournalRefTypeEnumV2(57).name
    assert JournalRefTypeEnumV2(58).name
    assert JournalRefTypeEnumV2(59).name
    assert JournalRefTypeEnumV2(60).name
    assert JournalRefTypeEnumV2(63).name
    assert JournalRefTypeEnumV2(64).name
    assert JournalRefTypeEnumV2(65).name
    assert JournalRefTypeEnumV2(66).name
    assert JournalRefTypeEnumV2(67).name
    assert JournalRefTypeEnumV2(68).name
    assert JournalRefTypeEnumV2(69).name
    assert JournalRefTypeEnumV2(70).name
    assert JournalRefTypeEnumV2(71).name
    assert JournalRefTypeEnumV2(72).name
    assert JournalRefTypeEnumV2(73).name
    assert JournalRefTypeEnumV2(74).name
    assert JournalRefTypeEnumV2(77).name
    assert JournalRefTypeEnumV2(78).name
    assert JournalRefTypeEnumV2(79).name
    assert JournalRefTypeEnumV2(80).name
    assert JournalRefTypeEnumV2(81).name
    assert JournalRefTypeEnumV2(82).name
    assert JournalRefTypeEnumV2(83).name
    assert JournalRefTypeEnumV2(84).name
    assert JournalRefTypeEnumV2(85).name
    assert JournalRefTypeEnumV2(86).name
    assert JournalRefTypeEnumV2(87).name
    assert JournalRefTypeEnumV2(88).name
    assert JournalRefTypeEnumV2(96).name
    assert JournalRefTypeEnumV2(97).name
    assert JournalRefTypeEnumV2(98).name
    assert JournalRefTypeEnumV2(99).name
    assert JournalRefTypeEnumV2(101).name
    assert JournalRefTypeEnumV2(102).name
    assert JournalRefTypeEnumV2(112).name
    assert JournalRefTypeEnumV2(113).name
    assert JournalRefTypeEnumV2(114).name
    assert JournalRefTypeEnumV2(115).name
    assert JournalRefTypeEnumV2(116).name
    assert JournalRefTypeEnumV2(117).name
    assert JournalRefTypeEnumV2(120).name
    assert JournalRefTypeEnumV2(122).name
    assert JournalRefTypeEnumV2(123).name
    assert JournalRefTypeEnumV2(124).name
    assert JournalRefTypeEnumV2(125).name
    assert JournalRefTypeEnumV2(127).name
    assert JournalRefTypeEnumV2(128).name
    assert JournalRefTypeEnumV2(129).name


def test_extra_info():
    assert populate_extra_info(1, "test", 123) == \
        {"location_id": 123}
    assert populate_extra_info(1, None, None) == {}

    assert populate_extra_info(233, "abc", 123) == \
        {"argument_name": "abc", "argument_value": 123}
