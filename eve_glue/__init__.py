"""EVE-specific helpers for ESI endpoints."""


from datetime import datetime

from eve_glue.location_type import resolve_location_type_enum  # noqa
from eve_glue.location_flag import PersonalLocationFlagEnumV1  # noqa
from eve_glue.location_flag import PersonalLocationFlagEnumV2  # noqa
from eve_glue.location_flag import CorporationLocationFlagEnumV1  # noqa
from eve_glue.location_flag import CorporationLocationFlagEnumV2  # noqa
from eve_glue.location_flag import FittingLocationFlagEnumV1  # noqa
from eve_glue.wallet_journal_ref import JournalRefTypeEnumV2  # noqa
from eve_glue.wallet_journal_ref import populate_extra_info  # noqa
from eve_glue.notification_type import NotificationTypeEnumV2  # noqa
from eve_glue.containers import ActionsEnumV1, PasswordTypeEnumV1  # noqa
from eve_glue.poco import StructureStateEnumV1  # noqa
from eve_glue.faction_warfare import SystemContestationState  # noqa


# EVE Online was released on May 6, 2003
# this specific time is used in place of None where an
# attribute must be returned as dt but no time data exists
EPOCH = 1052179200
EPOCH_DT = datetime.utcfromtimestamp(EPOCH)
EPOCH_STR = EPOCH_DT.strftime("%Y-%m-%dT%H:%M:%SZ")
