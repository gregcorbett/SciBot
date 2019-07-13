"""This file defines the CommandLog class."""

from src.CustomEvent import CustomEvent
from src.Icon import Icon
from src.IconGroup import IconGroup


class CommandLog(IconGroup):
    """This class defines a store for all the command log entries."""

    def __init__(self, screen_location, size):
        """Create a new CommandLog."""
        self.screen_location = screen_location
        # This is the size of the CommandLog.
        self.size = size
        # The Icon's size will be equal to the minimum dimension of
        # this CommandLog. This will allow Icon's to stack regardless
        # of wether the CommandLog is "veritcal" or "horizontal".
        self.horizontal = self.size[0] > self.size[1]
        minimum_dimension = min(self.size[0], self.size[1])
        self.icon_size = (minimum_dimension, minimum_dimension)
        super().__init__()

    def update(self, beebot_memory):
        """Update the CommandLog to match the given BeeBot memory."""
        # A BeeBot's memory should only be appended to or cleared entirely.
        # As such, we only need to update the CommandLog if the number of
        # commands in the BeeBot does not match the number of the commands
        # currently in the CommandLog.
        if len(self.icons) != len(beebot_memory):
            # We need to rebuild the CommandLog, so we must clear it first.
            self.removal_all()
            # Rebild the CommandLog
            self._convert_memory_to_icons(beebot_memory)

    def _convert_memory_to_icons(self, beebot_memory):
        """Convert the BeeBot memory into Icons."""
        # The location to draw the first Icon in the CommandLog.
        location = self.screen_location

        if self.horizontal:
            # Make the next Icon appear right of the current one.
            increment = (self.icon_size[0], 0)
        else:
            # Make the next Icon appear below the current one.
            increment = (0, self.icon_size[1])

        for index, entry in enumerate(beebot_memory):
            # Convert Events into Icon Arrows.
            text = self._event_type_to_text(entry.type)
            # Create a new Icon
            tmp_log = Icon(text, (0, 0, 0), (255, 255, 255),
                           location, self.icon_size)

            # Add the Icon to the CommandLog.
            # We need to provide a key here because instances of CommandLog
            # will have multiple Icons with the same text (i.e.
            # "Forward", "Backward", "Turn Left", "Turn Right")
            # that would otherwise override each other.
            self.add(tmp_log, key=index)

            # Put the next Icon in the right place
            location = location + increment

    @classmethod
    def _event_type_to_text(cls, event_type):
        """Return text based on the provided event type."""
        # A dictionary mapping event_types to text
        event_type_dict = {
            CustomEvent.MOVE_BEEBOT_UP: "Forward",
            CustomEvent.MOVE_BEEBOT_LEFT: "Turn Left",
            CustomEvent.MOVE_BEEBOT_RIGHT: "Turn Right",
            CustomEvent.MOVE_BEEBOT_DOWN: "Backward",
        }

        return event_type_dict[event_type]
