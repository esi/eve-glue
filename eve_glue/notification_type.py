NOTIFICATION_TYPE_TO_ENUM = {
    1: OldLscMessages,
    2: CharTerminationMsg,
    3: CharMedalMsg,
    4: AllMaintenanceBillMsg,
    5: AllWarDeclaredMsg,
    6: AllWarSurrenderMsg,
    7: AllWarRetractedMsg,
    8: AllWarInvalidatedMsg,
    10: CorpAllBillMsg,
    11: BillOutOfMoneyMsg,
    13: BillPaidCorpAllMsg,
    14: BountyClaimMsg,
    15: CloneActivationMsg,
    16: CorpAppNewMsg,
    17: CorpAppRejectMsg,
    18: CorpAppAcceptMsg,
    19: CorpTaxChangeMsg,
    20: CorpNewsMsg,
    21: CharLeftCorpMsg,
    22: CorpNewCEOMsg,
    23: CorpDividendMsg,
    25: CorpVoteMsg,
    26: CorpVoteCEORevokedMsg,
    27: CorpWarDeclaredMsg,
    28: CorpWarFightingLegalMsg,
    29: CorpWarSurrenderMsg,
    30: CorpWarRetractedMsg,
    31: CorpWarInvalidatedMsg,
    32: ContainerPasswordMsg,
    33: CustomsMsg,
    34: InsuranceFirstShipMsg,
    35: InsurancePayoutMsg,
    36: InsuranceInvalidatedMsg,
    38: SovCorpClaimFailMsg,
    40: SovCorpBillLateMsg,
    41: SovAllClaimLostMsg,
    43: SovAllClaimAquiredMsg,
    45: AllAnchoringMsg,
    46: AllStructVulnerableMsg,
    47: AllStrucInvulnerableMsg,
    48: SovDisruptorMsg,
    49: CorpStructLostMsg,
    50: CorpOfficeExpirationMsg,
    51: CloneRevokedMsg1,
    52: CloneMovedMsg,
    53: CloneRevokedMsg2,
    54: InsuranceExpirationMsg,
    55: InsuranceIssuedMsg,
    56: JumpCloneDeletedMsg1,
    57: JumpCloneDeletedMsg2,
    58: FWCorpJoinMsg,
    59: FWCorpLeaveMsg,
    60: FWCorpKickMsg,
    61: FWCharKickMsg,
    62: FWCorpWarningMsg,
    63: FWCharWarningMsg,
    64: FWCharRankLossMsg,
    65: FWCharRankGainMsg,
    67: TransactionReversalMsg,
    68: ReimbursementMsg,
    69: LocateCharMsg,
    70: ResearchMissionAvailableMsg,
    71: MissionOfferExpirationMsg,
    72: MissionTimeoutMsg,
    73: StoryLineMissionAvailableMsg,
    74: TutorialMsg,
    75: TowerAlertMsg,
    76: TowerResourceAlertMsg,
    77: StationAggressionMsg1,
    78: StationStateChangeMsg,
    79: StationConquerMsg,
    80: StationAggressionMsg2,
    81: FacWarCorpJoinRequestMsg,
    82: FacWarCorpLeaveRequestMsg,
    83: FacWarCorpJoinWithdrawMsg,
    84: FacWarCorpLeaveWithdrawMsg,
    85: CorpLiquidationMsg,
    86: SovereigntyTCUDamageMsg,
    87: SovereigntySBUDamageMsg,
    88: SovereigntyIHDamageMsg,
    89: ContactAdd,
    90: ContactEdit,
    91: IncursionCompletedMsg,
    92: CorpKicked,
    93: OrbitalAttacked,
    94: OrbitalReinforced,
    95: OwnershipTransferred,
    96: FWAllianceWarningMsg,
    97: FWAllianceKickMsg,
    98: AllWarCorpJoinedAllianceMsg,
    99: AllyJoinedWarDefenderMsg,
    100: AllyJoinedWarAggressorMsg,
    101: AllyJoinedWarAllyMsg,
    102: MercOfferedNegotiationMsg,
    103: WarSurrenderOfferMsg,
    104: WarSurrenderDeclinedMsg,
    105: FacWarLPPayoutKill,
    106: FacWarLPPayoutEvent,
    107: FacWarLPDisqualifiedEvent,
    108: FacWarLPDisqualifiedKill,
    109: AllyContractCancelled,
    110: WarAllyOfferDeclinedMsg,
    111: BountyYourBountyClaimed,
    112: BountyPlacedChar,
    113: BountyPlacedCorp,
    114: BountyPlacedAlliance,
    115: KillRightAvailable,
    116: KillRightAvailableOpen,
    117: KillRightEarned,
    118: KillRightUsed,
    119: KillRightUnavailable,
    120: KillRightUnavailableOpen,
    121: DeclareWar,
    122: OfferedSurrender,
    123: AcceptedSurrender,
    124: MadeWarMutual,
    125: RetractsWar,
    126: OfferedToAlly,
    127: AcceptedAlly,
    128: CharAppAcceptMsg,
    129: CharAppRejectMsg,
    130: CharAppWithdrawMsg,
    131: DustAppAcceptedMsg,
    132: DistrictAttacked,
    133: BattlePunishFriendlyFire,
    134: BountyESSTaken,
    135: BountyESSShared,
    136: IndustryTeamAuctionWon,
    137: IndustryTeamAuctionLost,
    138: CloneActivationMsg2,
    139: CorpAppInvitedMsg,
    140: KillReportVictim,
    141: KillReportFinalBlow,
    142: CorpAppRejectCustomMsg,
    143: CorpFriendlyFireEnableTimerStarted,
    144: CorpFriendlyFireDisableTimerStarted,
    145: CorpFriendlyFireEnableTimerCompleted,
    146: CorpFriendlyFireDisableTimerCompleted,
    147: EntosisCaptureStarted,
    148: StationServiceEnabled,
    149: StationServiceDisabled,
    152: InfrastructureHubBillAboutToExpire,
    160: SovStructureReinforced,
    161: SovCommandNodeEventStarted,
    162: SovStructureDestroyed,
    163: SovStationEnteredFreeport,
    164: IHubDestroyedByBillFailure,
    165: AllianceCapitalChanged,
    166: BuddyConnectContactAdd,
    167: SovStructureSelfDestructRequested,
    168: SovStructureSelfDestructCancel,
    169: SovStructureSelfDestructFinished,
    181: StructureFuelAlert,
    182: StructureAnchoring,
    183: StructureUnanchoring,
    184: StructureUnderAttack,
    185: StructureOnline,
    186: StructureLostShields,
    187: StructureLostArmor,
    188: StructureDestroyed,
    198: StructureServicesOffline,
    199: StructureItemsDelivered,
    200: SeasonalChallengeCompleted,
    201: StructureCourierContractChanged,
    1012: OperationFinished,
    1022: GiftReceived,
    1030: GameTimeReceived,
    1031: GameTimeSent,
    1032: GameTimeAdded,
    3001: NPCStandingsLost,
    3002: NPCStandingsGained,
}

def resolve_notification_type_enum(notification_type_id):
    try:
        return NOTIFICATION_TYPE_TO_ENUM[notification_type_id]
    except:
        return "unknown"