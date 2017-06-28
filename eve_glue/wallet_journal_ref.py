JOURNAL_REF_TYPE_TO_ENUM = {
    1: "player_trading",
    2: "market_transaction",
    10: "player_donation",
    13: "office_rental_fee",
    17: "bounty_prize_historical",
    19: "insurance",
    33: "mission_reward",
    34: "mission_reward_bonus",
    35: "cspa",
    37: "corp_account_withdrawal",
    40: "logo_change_fee",
    42: "market_escrow",
    46: "broker_fee",
    50: "alliance_maintenance_fee",
    54: "sales_tax",
    55: "jump_clone_installation_fee",
    56: "manufacturing",
    63: "contract",
    64: "contract",
    71: "contract",
    72: "contract",
    73: "contract",
    74: "contract",
    79: "contract",
    80: "contract",
    81: "contract",
    82: "contract",
    85: "bounty_prizes",
    87: "medal_creation_fee",
    88: "medal_issuing_fee",
    96: "customs_office_import_duty",
    97: "customs_office_export_duty",
    99: "corporate_reward_payout",
    120: "industry_facility_tax",
    125: "project_discovery_reward",
    127: "reprocessing_fee",
    128: "jump_clone_activation_fee",
}


def resolve_journal_ref_type_enum(ref_type_id):
    """
    ref_type:
        type: string
        description: Transaction type
        enum:
            - player_trading
            - market_transaction
            - player_donation
            - office_rental_fee
            - bounty_prize_historical
            - insurance
            - mission_reward
            - mission_reward_bonus
            - cspa
            - corp_account_withdrawal
            - logo_change_fee
            - market_escrow
            - broker_fee
            - alliance_maintenance_fee
            - sales_tax
            - jump_clone_installation_fee
            - manufacturing
            - contract
            - bounty_prizes
            - medal_creation_fee
            - medal_issuing_fee
            - customs_office_import_duty
            - customs_office_export_duty
            - corporate_reward_payout
            - industry_facility_tax
            - project_discovery_reward
            - reprocessing_fee
            - jump_clone_activation_fee
            - unknown
    """
    return JOURNAL_REF_TYPE_TO_ENUM.get(ref_type_id, "unknown")


def populate_extra_info(ref_type_id, arg_name, arg_value):
    """
    extra_info:
        type: object
        description: Extra information for different type of transaction
        properties:
            location_id:
                type: integer
                format: int64
            transaction_id:
                type: integer
                format: int64
            npc_name:
                type: string
            npc_id:
                type: integer
                format: int32
            destroyed_ship_type_id:
                type: integer
                format: int32
            character_id:
                type: integer
                format: int32
            corporation_id:
                type: integer
                format: int32
            alliance_id:
                type: integer
                format: int32
            job_id:
                type: integer
                format: int32
            contract_id:
                type: integer
                format: int32
            system_id:
                type: integer
                format: int32
            planet_id:
                type: integer
                format: int32
            argument_name:
                type: string
                description: Raw values if ESI couldn't resolve the ref_type
            argument_value:
                type: integer
                format: int64
                description: Raw values if ESI couldn't resolve the ref_type
    """
    extra_info = {}

    def _unpack_str(to_key, value):
        if value is not None:
            extra_info[to_key] = value

    def _unpack_int(to_key, value):
        if value is not None:
            extra_info[to_key] = int(value)

    if ref_type_id in [1, 120]:
        _unpack_int("location_id", arg_value)
    elif ref_type_id == 2:
        _unpack_int("transaction_id", arg_value)
    elif ref_type_id in [10, 42, 54, 99, 127, 13, 46, 55, 125, 128]:
        pass
    elif ref_type_id == 17:
        _unpack_str("npc_name", arg_name)
        _unpack_int("npc_id", arg_value)
    elif ref_type_id == 19:
        _unpack_int("destroyed_ship_type_id", arg_name)
    elif ref_type_id in [33, 34, 35, 37, 87, 88]:
        _unpack_int("character_id", arg_value)
    elif ref_type_id == 40:
        _unpack_int("corporation_id", arg_value)
    elif ref_type_id == 50:
        _unpack_int("alliance_id", arg_value)
    elif ref_type_id == 56:
        _unpack_int("job_id", arg_name)
    elif ref_type_id in [63, 64, 71, 72, 73, 74, 79, 80, 81, 82]:
        _unpack_int("contract_id", arg_name)
    elif ref_type_id == 85:
        _unpack_int("system_id", arg_value)
    elif ref_type_id in [96, 97]:
        _unpack_int("planet_id", arg_value)
    else:
        _unpack_str("argument_name", arg_name)
        _unpack_int("argument_value", arg_value)

    return extra_info

