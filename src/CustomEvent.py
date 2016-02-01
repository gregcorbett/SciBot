"""This file contains the CustomEvent class."""
from enum import IntEnum
from pygame import USEREVENT


class CustomEvent(IntEnum):
    """A class of IntEnums for locally defined events, such as RUN_FAIL."""

    # BeeBot movement events
    MOVE_BEEBOT_UP = USEREVENT + 1
    MOVE_BEEBOT_LEFT = USEREVENT + 2
    MOVE_BEEBOT_DOWN = USEREVENT + 3
    MOVE_BEEBOT_RIGHT = USEREVENT + 4

    # Win / Fail events
    RUN_FAIL = USEREVENT + 5
    RUN_WIN = USEREVENT + 6
