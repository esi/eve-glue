"""Helpers for mapping calendar event IDs to names."""


import enum


class EventResponse(enum.Enum):
    """Enum to describe the options when responding to an event invite."""

    declined = 2
    not_responded = 3
    accepted = 4
    tentative = 5


EVENT_OWNERS = {
    0: "eve_server",
    2: "corporation",
    30: "faction",
    1373: "character",
    1374: "character",
    1375: "character",
    1376: "character",
    1377: "character",
    1378: "character",
    1379: "character",
    1380: "character",
    1381: "character",
    1382: "character",
    1383: "character",
    1384: "character",
    1385: "character",
    1386: "character",
    16159: "alliance",
    34574: "character",
}
