"""Helpers for corporation roles."""


import enum

from eve_glue.bitmask import mask_list


class CorpRolesEnum(enum.Enum):
    """Map of role name to role bit."""

    Director = 1
    Personnel_Manager = 128
    Accountant = 256
    Security_Officer = 512
    Factory_Manager = 1024
    Station_Manager = 2048
    Auditor = 4096
    Hangar_Take_1 = 8192
    Hangar_Take_2 = 16384
    Hangar_Take_3 = 32768
    Hangar_Take_4 = 65536
    Hangar_Take_5 = 131072
    Hangar_Take_6 = 262144
    Hangar_Take_7 = 524288
    Hangar_Query_1 = 1048576
    Hangar_Query_2 = 2097152
    Hangar_Query_3 = 4194304
    Hangar_Query_4 = 8388608
    Hangar_Query_5 = 16777216
    Hangar_Query_6 = 33554432
    Hangar_Query_7 = 67108864
    Account_Take_1 = 134217728
    Account_Take_2 = 268435456
    Account_Take_3 = 536870912
    Account_Take_4 = 1073741824
    Account_Take_5 = 2147483648
    Account_Take_6 = 4294967296
    Account_Take_7 = 8589934592
    Diplomat = 17179869184
    Config_Equipment = 2199023255552
    Container_Take_1 = 4398046511104
    Container_Take_2 = 8796093022208
    Container_Take_3 = 17592186044416
    Container_Take_4 = 35184372088832
    Container_Take_5 = 70368744177664
    Container_Take_6 = 140737488355328
    Container_Take_7 = 281474976710656
    Rent_Office = 562949953421312
    Rent_Factory_Facility = 1125899906842624
    Rent_Research_Facility = 2251799813685248
    Junior_Accountant = 4503599627370496
    Config_Starbase_Equipment = 9007199254740992
    Trader = 18014398509481984
    Communications_Officer = 36028797018963968
    Contract_Manager = 72057594037927936
    Starbase_Defense_Operator = 144115188075855872
    Starbase_Fuel_Technician = 288230376151711744
    Fitting_Manager = 576460752303423488
    Terrestrial_Combat_Officer = 1152921504606846976
    Terrestrial_Logistics_Officer = 2305843009213693952


def calc_roles_from_mask(mask):
    """Return a list of role names from a roles mask."""

    roles = []
    for role in mask_list(mask):
        try:
            roles.append(CorpRolesEnum(role).name)
        except ValueError:
            pass

    return roles
