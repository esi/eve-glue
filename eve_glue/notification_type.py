"""Helpers for character notifications."""

import enum

from eve_glue.enums import new_from_enum


class NotificationTypeEnumV2(enum.Enum):
    """Maps notification type IDs to names."""

    OldLscMessages = 1
    CharTerminationMsg = 2
    CharMedalMsg = 3
    AllMaintenanceBillMsg = 4
    AllWarDeclaredMsg = 5
    AllWarSurrenderMsg = 6
    AllWarRetractedMsg = 7
    AllWarInvalidatedMsg = 8
    CorpAllBillMsg = 10
    BillOutOfMoneyMsg = 11
    BillPaidCorpAllMsg = 13
    BountyClaimMsg = 14
    CloneActivationMsg = 15
    CorpAppNewMsg = 16
    CorpAppRejectMsg = 17
    CorpAppAcceptMsg = 18
    CorpTaxChangeMsg = 19
    CorpNewsMsg = 20
    CharLeftCorpMsg = 21
    CorpNewCEOMsg = 22
    CorpDividendMsg = 23
    CorpVoteMsg = 25
    CorpVoteCEORevokedMsg = 26
    CorpWarDeclaredMsg = 27
    CorpWarFightingLegalMsg = 28
    CorpWarSurrenderMsg = 29
    CorpWarRetractedMsg = 30
    CorpWarInvalidatedMsg = 31
    ContainerPasswordMsg = 32
    CustomsMsg = 33
    InsuranceFirstShipMsg = 34
    InsurancePayoutMsg = 35
    InsuranceInvalidatedMsg = 36
    SovCorpClaimFailMsg = 38
    SovCorpBillLateMsg = 40
    SovAllClaimLostMsg = 41
    SovAllClaimAquiredMsg = 43
    AllAnchoringMsg = 45
    AllStructVulnerableMsg = 46
    AllStrucInvulnerableMsg = 47
    SovDisruptorMsg = 48
    CorpStructLostMsg = 49
    CorpOfficeExpirationMsg = 50
    CloneRevokedMsg1 = 51
    CloneMovedMsg = 52
    CloneRevokedMsg2 = 53
    InsuranceExpirationMsg = 54
    InsuranceIssuedMsg = 55
    JumpCloneDeletedMsg1 = 56
    JumpCloneDeletedMsg2 = 57
    FWCorpJoinMsg = 58
    FWCorpLeaveMsg = 59
    FWCorpKickMsg = 60
    FWCharKickMsg = 61
    FWCorpWarningMsg = 62
    FWCharWarningMsg = 63
    FWCharRankLossMsg = 64
    FWCharRankGainMsg = 65
    TransactionReversalMsg = 67
    ReimbursementMsg = 68
    LocateCharMsg = 69
    ResearchMissionAvailableMsg = 70
    MissionOfferExpirationMsg = 71
    MissionTimeoutMsg = 72
    StoryLineMissionAvailableMsg = 73
    TutorialMsg = 74
    TowerAlertMsg = 75
    TowerResourceAlertMsg = 76
    StationAggressionMsg1 = 77
    StationStateChangeMsg = 78
    StationConquerMsg = 79
    StationAggressionMsg2 = 80
    FacWarCorpJoinRequestMsg = 81
    FacWarCorpLeaveRequestMsg = 82
    FacWarCorpJoinWithdrawMsg = 83
    FacWarCorpLeaveWithdrawMsg = 84
    CorpLiquidationMsg = 85
    SovereigntyTCUDamageMsg = 86
    SovereigntySBUDamageMsg = 87
    SovereigntyIHDamageMsg = 88
    ContactAdd = 89
    ContactEdit = 90
    IncursionCompletedMsg = 91
    CorpKicked = 92
    OrbitalAttacked = 93
    OrbitalReinforced = 94
    OwnershipTransferred = 95
    FWAllianceWarningMsg = 96
    FWAllianceKickMsg = 97
    AllWarCorpJoinedAllianceMsg = 98
    AllyJoinedWarDefenderMsg = 99
    AllyJoinedWarAggressorMsg = 100
    AllyJoinedWarAllyMsg = 101
    MercOfferedNegotiationMsg = 102
    WarSurrenderOfferMsg = 103
    WarSurrenderDeclinedMsg = 104
    FacWarLPPayoutKill = 105
    FacWarLPPayoutEvent = 106
    FacWarLPDisqualifiedEvent = 107
    FacWarLPDisqualifiedKill = 108
    AllyContractCancelled = 109
    WarAllyOfferDeclinedMsg = 110
    BountyYourBountyClaimed = 111
    BountyPlacedChar = 112
    BountyPlacedCorp = 113
    BountyPlacedAlliance = 114
    KillRightAvailable = 115
    KillRightAvailableOpen = 116
    KillRightEarned = 117
    KillRightUsed = 118
    KillRightUnavailable = 119
    KillRightUnavailableOpen = 120
    DeclareWar = 121
    OfferedSurrender = 122
    AcceptedSurrender = 123
    MadeWarMutual = 124
    RetractsWar = 125
    OfferedToAlly = 126
    AcceptedAlly = 127
    CharAppAcceptMsg = 128
    CharAppRejectMsg = 129
    CharAppWithdrawMsg = 130
    DustAppAcceptedMsg = 131
    DistrictAttacked = 132
    BattlePunishFriendlyFire = 133
    BountyESSTaken = 134
    BountyESSShared = 135
    IndustryTeamAuctionWon = 136
    IndustryTeamAuctionLost = 137
    CloneActivationMsg2 = 138
    CorpAppInvitedMsg = 139
    KillReportVictim = 140
    KillReportFinalBlow = 141
    CorpAppRejectCustomMsg = 142
    CorpFriendlyFireEnableTimerStarted = 143  # pylint: disable=invalid-name
    CorpFriendlyFireDisableTimerStarted = 144  # pylint: disable=invalid-name
    CorpFriendlyFireEnableTimerCompleted = 145  # pylint: disable=invalid-name
    CorpFriendlyFireDisableTimerCompleted = 146  # pylint: disable=invalid-name
    EntosisCaptureStarted = 147
    StationServiceEnabled = 148
    StationServiceDisabled = 149
    InfrastructureHubBillAboutToExpire = 152  # pylint: disable=invalid-name
    SovStructureReinforced = 160
    SovCommandNodeEventStarted = 161
    SovStructureDestroyed = 162
    SovStationEnteredFreeport = 163
    IHubDestroyedByBillFailure = 164
    AllianceCapitalChanged = 165
    BuddyConnectContactAdd = 166
    SovStructureSelfDestructRequested = 167  # pylint: disable=invalid-name
    SovStructureSelfDestructCancel = 168
    SovStructureSelfDestructFinished = 169  # pylint: disable=invalid-name
    StructureFuelAlert = 181
    StructureAnchoring = 182
    StructureUnanchoring = 183
    StructureUnderAttack = 184
    StructureOnline = 185
    StructureLostShields = 186
    StructureLostArmor = 187
    StructureDestroyed = 188
    StructureItemsMovedToSafety = 190
    StructureServicesOffline = 198
    StructureItemsDelivered = 199
    SeasonalChallengeCompleted = 200
    StructureCourierContractChanged = 201
    OperationFinished = 1012
    GiftReceived = 1022
    GameTimeReceived = 1030
    GameTimeSent = 1031
    GameTimeAdded = 1032
    NPCStandingsLost = 3001
    NPCStandingsGained = 3002
    MoonminingExtractionStarted = 202
    MoonminingExtractionCancelled = 203
    MoonminingExtractionFinished = 204
    MoonminingLaserFired = 205
    MoonminingAutomaticFracture = 206
    StructureWentLowPower = 207
    StructureWentHighPower = 208
    StructuresReinforcementChanged = 209


NotificationTypeEnumV3 = new_from_enum(  # pylint: disable=invalid-name
    "NotificationTypeEnumV3",
    NotificationTypeEnumV2,
    add={
        "StructuresJobsPaused": 210,
        "StructuresJobsCancelled": 211,
    },
)

NotificationTypeEnumV4 = new_from_enum(  # pylint: disable=invalid-name
    "NotificationTypeEnumV4",
    NotificationTypeEnumV3,
    add={
        "CombatOperationFinished": 1013,
        "IndustryOperationFinished": 1014,
        "ESSMainBankLink": 1015,
    },
)

NotificationTypeEnumV5 = new_from_enum(  # pylint: disable=invalid-name
    "NotificationTypeEnumV5",
    NotificationTypeEnumV4,
    add={
        "CorpBecameWarEligible": 221,
        "CorpNoLongerWarEligible": 222,
        "WarHQRemovedFromSpace": 223,
        "CorpWarDeclaredV2": 224,
        "AllianceWarDeclaredV2": 225,
    },
)

NotificationTypeEnumV6 = new_from_enum(  # pylint: disable=invalid-name
    "NotificationTypeEnumV6",
    NotificationTypeEnumV5,
    add={
        "InvasionSystemLogin": 226,
        "MutualWarInviteSent": 229,
        "MutualWarInviteRejected": 230,
        "MutualWarInviteAccepted": 231,
        "WarDeclared": 232,
        "WarAdopted ": 233,
        "MutualWarExpired": 234,
        "WarInherited": 235,
        "WarAllyInherited": 236,
        "WarConcordInvalidates": 237,
        "WarRetracted": 238,
        "WarRetractedByConcord": 239,
        "WarInvalid": 240,
    },
)

NotificationTypeEnumV7 = new_from_enum(  # pylint: disable=invalid-name
    "NotificationTypeEnumV7",
    NotificationTypeEnumV6,
    add={
        "MercOfferRetractedMsg": 241,
        "OfferToAllyRetracted": 242,
    },
)

NotificationTypeEnumV8 = new_from_enum(  # pylint: disable=invalid-name
    "NotificationTypeEnumV8",
    NotificationTypeEnumV7,
    add={
        "InvasionSystemStart": 227,
        "InvasionCompletedMsg": 228,
        "RaffleCreated": 243,
        "RaffleExpired": 244,
        "RaffleFinished": 245,
        "WarEndedHqSecurityDrop": 246,
        "MissionCanceledTriglavian": 247,
        "AgentRetiredTrigravian": 248,
        "StructureImpendingAbandonmentAssetsAtRisk": 249,
        "OfficeLeaseCanceledInsufficientStandings": 250,
        "ContractRegionChangedToPochven": 251,
    },
)

NotificationTypeEnumV9 = new_from_enum(  # pylint: disable=invalid-name
    "NotificationTypeEnumV9",
    NotificationTypeEnumV8,
    add={
        "ExpertSystemExpiryImminent": 252,
        "ExpertSystemExpired": 253,
    },
)

NotificationTypeEnumV10 = new_from_enum(
    "NotificationTypeEnumV10",
    NotificationTypeEnumV9,
    add={
        "StructurePaintPurchased": 254,
        "CorporationGoalCreated": 260,
        "CorporationGoalClosed": 261,
        "CorporationGoalCompleted": 262,
    },
)

NotificationTypeEnumV11 = new_from_enum(
    "NotificationTypeEnumV11",
    NotificationTypeEnumV10,
    add={
        "CorporationGoalNameChange": 263,
        "CorporationLeft": 270,
    },
)

NotificationTypeEnumV12 = new_from_enum(
    "NotificationTypeEnumV12",
    NotificationTypeEnumV11,
    add={
        "CorporationGoalExpired": 264,
        "CorporationGoalLimitReached": 265,
        "LPAutoRedeemed": 275,
        "SPAutoRedeemed": 276,
        "SkinSequencingCompleted": 280,
        "SkyhookOnline": 281,
        "SkyhookLostShields": 282,
        "SkyhookUnderAttack": 283,
        "SkyhookDestroyed": 284,
        "SkyhookDeployed": 285,
        "MercenaryDenReinforced": 286,
        "MercenaryDenAttacked": 287,
        "MercenaryDenNewMTO": 288,
        "FreelanceProjectClosed": 290,
        "FreelanceProjectCompleted": 292,
        "FreelanceProjectLimitReached": 293,
        "FreelanceProjectParticipantKicked": 294,
        "FreelanceProjectCreated": 295,
        "FreelanceProjectExpired": 296,
        "DailyItemRewardAutoClaimed": 6013,
        "StructureLowReagentsAlert": 6040,
        "StructureNoReagentsAlert": 6041,
    },
)
