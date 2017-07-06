JOURNAL_REF_TYPE_TO_ENUM = {
    1: "player_trading",
    2: "market_transaction",
    7: "mission_reward",
    8: "clone_activation",
    10: "player_donation",
    11: "corporation_payment",
    13: "office_rental_fee",
    14: "factory_slot_rental_fee",
    15: "repair_bill",
    16: "bounty",
    17: "bounty_prize",
    19: "insurance",
    20: "mission_expiration",
    21: "mission_completion",
    22: "shares",
    23: "courier_mission_escrow",
    24: "mission_cost",
    25: "agent_miscellaneous",
    26: "lp_store",
    27: "agent_location_services",
    28: "agent_donation",
    29: "agent_security_services",
    30: "agent_mission_collateral_paid",
    31: "agent_mission_collateral_refunded",
    32: "agents_preward",
    33: "agent_mission_reward",
    34: "agent_mission_time_bonus_reward",
    35: "cspa",
    36: "cspaofflinerefund",
    37: "corporation_account_withdrawal",
    38: "corporation_dividend_payment",
    39: "corporation_registration_fee",
    40: "corporation_logo_change_cost",
    41: "release_of_impounded_property",
    42: "market_escrow",
    43: "agent_services_rendered",
    44: "market_fine_paid",
    45: "corporation_liquidation",
    46: "brokers_fee",
    47: "corporation_bulk_payment",
    48: "alliance_registration_fee",
    49: "war_fee",
    50: "alliance_maintainance_fee",
    51: "contraband_fine",
    52: "clone_transfer",
    53: "acceleration_gate_fee",
    54: "transaction_tax",
    55: "jump_clone_installation_fee",
    56: "manufacturing",
    57: "researching_technology",
    58: "researching_time_productivity",
    59: "researching_material_productivity",
    60: "copying",
    62: "reverse_engineering",
    63: "contract_auction_bid",
    64: "contract_auction_bid_refund",
    65: "contract_collateral",
    66: "contract_reward_refund",
    67: "contract_auction_sold",
    68: "contract_reward",
    69: "contract_collateral_refund",
    70: "contract_collateral_payout",
    71: "contract_price",
    72: "contract_brokers_fee",
    73: "contract_sales_tax",
    74: "contract_deposit",
    75: "contract_deposit_sales_tax",
    77: "contract_auction_bid_corp",
    78: "contract_collateral_deposited_corp",
    79: "contract_price_payment_corp",
    80: "contract_brokers_fee_corp",
    81: "contract_deposit_corp",
    82: "contract_deposit_refund",
    83: "contract_reward_deposited",
    84: "contract_reward_deposited_corp",
    85: "bounty_prizes",
    86: "advertisement_listing_fee",
    87: "medal_creation",
    88: "medal_issued",
    90: "dna_modification_fee",
    91: "sovereignity_bill",
    92: "bounty_prize_corporation_tax",
    93: "agent_mission_reward_corporation_tax",
    94: "agent_mission_time_bonus_reward_corporation_tax",
    95: "upkeep_adjustment_fee",
    96: "planetary_import_tax",
    97: "planetary_export_tax",
    98: "planetary_construction",
    99: "corporate_reward_payout",
    101: "bounty_surcharge",
    103: "corporate_reward_tax",
    106: "store_purchase",
    107: "store_purchase_refund",
    112: "datacore_fee",
    113: "war_fee_surrender",
    114: "war_ally_contract",
    115: "bounty_reimbursement",
    116: "kill_right_fee",
    117: "security_processing_fee",
    120: "industry_job_tax",
    122: "infrastructure_hub_maintenance",
    123: "asset_safety_recovery_tax",
    124: "opportunity_reward",
    125: "project_discovery_reward",
    126: "project_discovery_tax",
    127: "reprocessing_tax",
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
            - mission_reward
            - clone_activation
            - player_donation
            - corporation_payment
            - office_rental_fee
            - factory_slot_rental_fee
            - repair_bill
            - bounty
            - bounty_prize
            - insurance
            - mission_expiration
            - mission_completion
            - shares
            - courier_mission_escrow
            - mission_cost
            - agent_miscellaneous
            - lp_store
            - agent_location_services
            - agent_donation
            - agent_security_services
            - agent_mission_collateral_paid
            - agent_mission_collateral_refunded
            - agents_preward
            - agent_mission_reward
            - agent_mission_time_bonus_reward
            - cspa
            - cspaofflinerefund
            - corporation_account_withdrawal
            - corporation_dividend_payment
            - corporation_registration_fee
            - corporation_logo_change_cost
            - release_of_impounded_property
            - market_escrow
            - agent_services_rendered
            - market_fine_paid
            - corporation_liquidation
            - brokers_fee
            - corporation_bulk_payment
            - alliance_registration_fee
            - war_fee
            - alliance_maintainance_fee
            - contraband_fine
            - clone_transfer
            - acceleration_gate_fee
            - transaction_tax
            - jump_clone_installation_fee
            - manufacturing
            - researching_technology
            - researching_time_productivity
            - researching_material_productivity
            - copying
            - reverse_engineering
            - contract_auction_bid
            - contract_auction_bid_refund
            - contract_collateral
            - contract_reward_refund
            - contract_auction_sold
            - contract_reward
            - contract_collateral_refund
            - contract_collateral_payout
            - contract_price
            - contract_brokers_fee
            - contract_sales_tax
            - contract_deposit
            - contract_deposit_sales_tax
            - contract_auction_bid_corp
            - contract_collateral_deposited_corp
            - contract_price_payment_corp
            - contract_brokers_fee_corp
            - contract_deposit_corp
            - contract_deposit_refund
            - contract_reward_deposited
            - contract_reward_deposited_corp
            - bounty_prizes
            - advertisement_listing_fee
            - medal_creation
            - medal_issued
            - dna_modification_fee
            - sovereignity_bill
            - bounty_prize_corporation_tax
            - agent_mission_reward_corporation_tax
            - agent_mission_time_bonus_reward_corporation_tax
            - upkeep_adjustment_fee
            - planetary_import_tax
            - planetary_export_tax
            - planetary_construction
            - corporate_reward_payout
            - bounty_surcharge
            - corporate_reward_tax
            - store_purchase
            - store_purchase_refund
            - datacore_fee
            - war_fee_surrender
            - war_ally_contract
            - bounty_reimbursement
            - kill_right_fee
            - security_processing_fee
            - industry_job_tax
            - infrastructure_hub_maintenance
            - asset_safety_recovery_tax
            - opportunity_reward
            - project_discovery_reward
            - project_discovery_tax
            - reprocessing_tax
            - jump_clone_activation_fee
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
