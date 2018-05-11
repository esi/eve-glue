"""Helpers for location IDs."""


import enum

from eve_glue.enums import new_from_enum


class PersonalLocationFlagEnumV1(enum.Enum):
    """Maps location names to IDs."""

    AutoFit = 0
    Wardrobe = 3
    Cargo = 5
    CorpseBay = 174
    DroneBay = 87
    FleetHangar = 155
    Deliveries = 173
    HiddenModifiers = 156
    Hangar = 4
    Module = 7
    HangarAll = 1000
    LoSlot0 = 11
    LoSlot1 = 12
    LoSlot2 = 13
    LoSlot3 = 14
    LoSlot4 = 15
    LoSlot5 = 16
    LoSlot6 = 17
    LoSlot7 = 18
    MedSlot0 = 19
    MedSlot1 = 20
    MedSlot2 = 21
    MedSlot3 = 22
    MedSlot4 = 23
    MedSlot5 = 24
    MedSlot6 = 25
    MedSlot7 = 26
    HiSlot0 = 27
    HiSlot1 = 28
    HiSlot2 = 29
    HiSlot3 = 30
    HiSlot4 = 31
    HiSlot5 = 32
    HiSlot6 = 33
    HiSlot7 = 34
    AssetSafety = 36
    Locked = 63
    Unlocked = 64
    Implant = 89
    QuafeBay = 154
    RigSlot0 = 92
    RigSlot1 = 93
    RigSlot2 = 94
    RigSlot3 = 95
    RigSlot4 = 96
    RigSlot5 = 97
    RigSlot6 = 98
    RigSlot7 = 99
    ShipHangar = 90
    SpecializedFuelBay = 133
    SpecializedOreHold = 134
    SpecializedGasHold = 135
    SpecializedMineralHold = 136
    SpecializedSalvageHold = 137
    SpecializedShipHold = 138
    SpecializedSmallShipHold = 139
    SpecializedMediumShipHold = 140
    SpecializedLargeShipHold = 141
    SpecializedIndustrialShipHold = 142
    SpecializedAmmoHold = 143
    SpecializedCommandCenterHold = 148
    SpecializedPlanetaryCommoditiesHold = 149  # pylint: disable=invalid-name
    SpecializedMaterialBay = 151
    SubSystemSlot0 = 125  # Core
    SubSystemSlot1 = 126  # Defensive
    SubSystemSlot2 = 127  # Offensive
    SubSystemSlot3 = 128  # Propulsion
    SubSystemSlot4 = 129
    SubSystemSlot5 = 130
    SubSystemSlot6 = 131
    SubSystemSlot7 = 132
    FighterBay = 158
    FighterTube0 = 159
    FighterTube1 = 160
    FighterTube2 = 161
    FighterTube3 = 162
    FighterTube4 = 163
    SubSystemBay = 177


class PersonalLocationFlagEnumV2(enum.Enum):
    """Maps location names to IDs."""

    AutoFit = 0
    Wardrobe = 3
    Hangar = 4
    Cargo = 5
    Skill = 7
    LoSlot0 = 11
    LoSlot1 = 12
    LoSlot2 = 13
    LoSlot3 = 14
    LoSlot4 = 15
    LoSlot5 = 16
    LoSlot6 = 17
    LoSlot7 = 18
    MedSlot0 = 19
    MedSlot1 = 20
    MedSlot2 = 21
    MedSlot3 = 22
    MedSlot4 = 23
    MedSlot5 = 24
    MedSlot6 = 25
    MedSlot7 = 26
    HiSlot0 = 27
    HiSlot1 = 28
    HiSlot2 = 29
    HiSlot3 = 30
    HiSlot4 = 31
    HiSlot5 = 32
    HiSlot6 = 33
    HiSlot7 = 34
    AssetSafety = 36
    Locked = 63
    Unlocked = 64
    DroneBay = 87
    Implant = 89
    ShipHangar = 90
    RigSlot0 = 92
    RigSlot1 = 93
    RigSlot2 = 94
    RigSlot3 = 95
    RigSlot4 = 96
    RigSlot5 = 97
    RigSlot6 = 98
    RigSlot7 = 99
    SubSystemSlot0 = 125  # Core
    SubSystemSlot1 = 126  # Defensive
    SubSystemSlot2 = 127  # Offensive
    SubSystemSlot3 = 128  # Propulsion
    SubSystemSlot4 = 129
    SubSystemSlot5 = 130
    SubSystemSlot6 = 131
    SubSystemSlot7 = 132
    SpecializedFuelBay = 133
    SpecializedOreHold = 134
    SpecializedGasHold = 135
    SpecializedMineralHold = 136
    SpecializedSalvageHold = 137
    SpecializedShipHold = 138
    SpecializedSmallShipHold = 139
    SpecializedMediumShipHold = 140
    SpecializedLargeShipHold = 141
    SpecializedIndustrialShipHold = 142
    SpecializedAmmoHold = 143
    SpecializedCommandCenterHold = 148
    SpecializedPlanetaryCommoditiesHold = 149  # pylint: disable=invalid-name
    SpecializedMaterialBay = 151
    QuafeBay = 154
    FleetHangar = 155
    HiddenModifiers = 156
    FighterBay = 158
    FighterTube0 = 159
    FighterTube1 = 160
    FighterTube2 = 161
    FighterTube3 = 162
    FighterTube4 = 163
    Deliveries = 173
    CorpseBay = 174
    SubSystemBay = 177
    HangarAll = 1000


class CorporationLocationFlagEnumV1(enum.Enum):
    """From inventorycommon/const.py:75."""

    AutoFit = 0
    Wallet = 1
    OfficeFolder = 2
    Wardrobe = 3
    Hangar = 4
    Cargo = 5
    Impounded = 6
    Skill = 7
    Reward = 8
    LoSlot0 = 11
    LoSlot1 = 12
    LoSlot2 = 13
    LoSlot3 = 14
    LoSlot4 = 15
    LoSlot5 = 16
    LoSlot6 = 17
    LoSlot7 = 18
    MedSlot0 = 19
    MedSlot1 = 20
    MedSlot2 = 21
    MedSlot3 = 22
    MedSlot4 = 23
    MedSlot5 = 24
    MedSlot6 = 25
    MedSlot7 = 26
    HiSlot0 = 27
    HiSlot1 = 28
    HiSlot2 = 29
    HiSlot3 = 30
    HiSlot4 = 31
    HiSlot5 = 32
    HiSlot6 = 33
    HiSlot7 = 34
    AssetSafety = 36
    Capsule = 56
    Pilot = 57
    SkillInTraining = 61
    CorpDeliveries = 62
    Locked = 63
    Unlocked = 64
    Bonus = 86
    DroneBay = 87
    Booster = 88
    Implant = 89
    ShipHangar = 90
    ShipOffline = 91
    RigSlot0 = 92
    RigSlot1 = 93
    RigSlot2 = 94
    RigSlot3 = 95
    RigSlot4 = 96
    RigSlot5 = 97
    RigSlot6 = 98
    RigSlot7 = 99
    CorpSAG1 = 115
    CorpSAG2 = 116
    CorpSAG3 = 117
    CorpSAG4 = 118
    CorpSAG5 = 119
    CorpSAG6 = 120
    CorpSAG7 = 121
    SecondaryStorage = 122
    SubSystemSlot0 = 125  # Core
    SubSystemSlot1 = 126  # Defensive
    SubSystemSlot2 = 127  # Offensive
    SubSystemSlot3 = 128  # Propulsion
    SubSystemSlot4 = 129  # Unused
    SubSystemSlot5 = 130  # Unused
    SubSystemSlot6 = 131  # Unused
    SubSystemSlot7 = 132  # Unused
    SpecializedFuelBay = 133
    SpecializedOreHold = 134
    SpecializedGasHold = 135
    SpecializedMineralHold = 136
    SpecializedSalvageHold = 137
    SpecializedShipHold = 138
    SpecializedSmallShipHold = 139
    SpecializedMediumShipHold = 140
    SpecializedLargeShipHold = 141
    SpecializedIndustrialShipHold = 142
    SpecializedAmmoHold = 143
    StructureActive = 144
    StructureInactive = 145
    JunkyardReprocessed = 146
    JunkyardTrashed = 147
    SpecializedCommandCenterHold = 148
    SpecializedPlanetaryCommoditiesHold = 149  # pylint: disable=invalid-name
    PlanetSurface = 150
    SpecializedMaterialBay = 151
    DustDatabank = 152
    DustBattle = 153
    QuafeBay = 154
    FleetHangar = 155
    HiddenModifers = 156
    StructureOffline = 157
    FighterBay = 158
    FighterTube0 = 159
    FighterTube1 = 160
    FighterTube2 = 161
    FighterTube3 = 162
    FighterTube4 = 163
    ServiceSlot0 = 164
    ServiceSlot1 = 165
    ServiceSlot2 = 166
    ServiceSlot3 = 167
    ServiceSlot4 = 168
    ServiceSlot5 = 169
    ServiceSlot6 = 170
    ServiceSlot7 = 171
    StructureFuel = 172
    Deliveries = 173
    CrateLoot = 174
    CorpseBay = 174
    BoosterBay = 176
    SubsystemBay = 177
    HangarAll = 1000


CorporationLocationFlagEnumV2 = new_from_enum(  # pylint: disable=invalid-name
    "CorporationLocationFlagEnumV2",
    CorporationLocationFlagEnumV1,
    remove=["HiddenModifers", "SubsystemBay"],
    add={
        "HiddenModifiers": 156,
        "SubSystemBay": 177
    }
)
