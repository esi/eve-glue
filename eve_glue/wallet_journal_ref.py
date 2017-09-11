import enum


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


def resolve_journal_ref_type_enum_v1(ref_type_id):
    """
    deprecated!!
    """
    return JOURNAL_REF_TYPE_TO_ENUM.get(ref_type_id, "unknown")


class JournalRefTypeEnumV2(enum.Enum):
    """
    ref_type:
        type: string
        description: Transaction type
        enum:
            - player_trading
            - market_transaction
            - gm_cash_transfer
            - mission_reward
            - clone_activation
            - inheritance
            - player_donation
            - corporation_payment
            - docking_fee
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
            - contract_reversal
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
            - operation_bonus
    """
    player_trading = 1
    market_transaction = 2
    gm_cash_transfer = 3
    mission_reward = 7
    clone_activation = 8
    inheritance = 9
    player_donation = 10
    corporation_payment = 11
    docking_fee = 12
    office_rental_fee = 13
    factory_slot_rental_fee = 14
    repair_bill = 15
    bounty = 16
    bounty_prize = 17
    insurance = 19
    mission_expiration = 20
    mission_completion = 21
    shares = 22
    courier_mission_escrow = 23
    mission_cost = 24
    agent_miscellaneous = 25
    lp_store = 26
    agent_location_services = 27
    agent_donation = 28
    agent_security_services = 29
    agent_mission_collateral_paid = 30
    agent_mission_collateral_refunded = 31
    agents_preward = 32
    agent_mission_reward = 33
    agent_mission_time_bonus_reward = 34
    cspa = 35
    cspaofflinerefund = 36
    corporation_account_withdrawal = 37
    corporation_dividend_payment = 38
    corporation_registration_fee = 39
    corporation_logo_change_cost = 40
    release_of_impounded_property = 41
    market_escrow = 42
    agent_services_rendered = 43
    market_fine_paid = 44
    corporation_liquidation = 45
    brokers_fee = 46
    corporation_bulk_payment = 47
    alliance_registration_fee = 48
    war_fee = 49
    alliance_maintainance_fee = 50
    contraband_fine = 51
    clone_transfer = 52
    acceleration_gate_fee = 53
    transaction_tax = 54
    jump_clone_installation_fee = 55
    manufacturing = 56
    researching_technology = 57
    researching_time_productivity = 58
    researching_material_productivity = 59
    copying = 60
    reverse_engineering = 62
    contract_auction_bid = 63
    contract_auction_bid_refund = 64
    contract_collateral = 65
    contract_reward_refund = 66
    contract_auction_sold = 67
    contract_reward = 68
    contract_collateral_refund = 69
    contract_collateral_payout = 70
    contract_price = 71
    contract_brokers_fee = 72
    contract_sales_tax = 73
    contract_deposit = 74
    contract_deposit_sales_tax = 75
    contract_auction_bid_corp = 77
    contract_collateral_deposited_corp = 78
    contract_price_payment_corp = 79
    contract_brokers_fee_corp = 80
    contract_deposit_corp = 81
    contract_deposit_refund = 82
    contract_reward_deposited = 83
    contract_reward_deposited_corp = 84
    bounty_prizes = 85
    advertisement_listing_fee = 86
    medal_creation = 87
    medal_issued = 88
    dna_modification_fee = 90
    sovereignity_bill = 91
    bounty_prize_corporation_tax = 92
    agent_mission_reward_corporation_tax = 93
    agent_mission_time_bonus_reward_corporation_tax = 94
    upkeep_adjustment_fee = 95
    planetary_import_tax = 96
    planetary_export_tax = 97
    planetary_construction = 98
    corporate_reward_payout = 99
    bounty_surcharge = 101
    contract_reversal = 102
    corporate_reward_tax = 103
    store_purchase = 106
    store_purchase_refund = 107
    datacore_fee = 112
    war_fee_surrender = 113
    war_ally_contract = 114
    bounty_reimbursement = 115
    kill_right_fee = 116
    security_processing_fee = 117
    industry_job_tax = 120
    infrastructure_hub_maintenance = 122
    asset_safety_recovery_tax = 123
    opportunity_reward = 124
    project_discovery_reward = 125
    project_discovery_tax = 126
    reprocessing_tax = 127
    jump_clone_activation_fee = 128
    operation_bonus = 129


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
        _unpack_int("character_id", arg_value)
    elif ref_type_id == 19:
        if int(arg_name) > 0:
            _unpack_int("destroyed_ship_type_id", arg_name)
    elif ref_type_id in [33, 34, 35, 37, 87, 88]:
        _unpack_int("character_id", arg_value)
    elif ref_type_id == 40:
        _unpack_int("corporation_id", arg_value)
    elif ref_type_id == 50:
        _unpack_int("alliance_id", arg_value)
    elif ref_type_id == 56:
        _unpack_int("job_id", arg_name)
    elif ref_type_id in range(63, 85):
        _unpack_int("contract_id", arg_name)
    elif ref_type_id == 85:
        _unpack_int("system_id", arg_value)
    elif ref_type_id in [96, 97]:
        _unpack_int("planet_id", arg_value)
    else:
        _unpack_str("argument_name", arg_name)
        _unpack_int("argument_value", arg_value)

    return extra_info
