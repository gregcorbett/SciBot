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

            # The location to draw the first Icon in the CommandLog.
            location = self.screen_location

            # The Icon's size will be equal to the minimum dimension of
            # this CommandLog. This will allow Icon's to stack regardless
            # of wether the CommandLog is "veritcal" or "horizontal".
            horizontal = self.size[0] > self.size[1]
            if horizontal:
                # Then the minimum dimension is the height
                minimum_dimension = self.size[1]
            else:
                # Then the minimum dimension is the width
                minimum_dimension = self.size[0]

            icon_size = (minimum_dimension, minimum_dimension)

            for index, entry in enumerate(beebot_memory):
                # Convert Events into Icon Arrows.
                if entry.type == CustomEvent.MOVE_BEEBOT_UP:
                    text = "Forward"

                if entry.type == CustomEvent.MOVE_BEEBOT_DOWN:
                    text = "Backward"

                if entry.type == CustomEvent.MOVE_BEEBOT_LEFT:
                    text = "Turn Left"

                if entry.type == CustomEvent.MOVE_BEEBOT_RIGHT:
                    text = "Turn Right"

                # Create a new Icon
                tmp_log = Icon(text, (0, 0, 0), (255, 255, 255),
                               location, icon_size)

                # Add the Icon to the CommandLog.
                # We need to provide a key here because instances of CommandLog
                # will have multiple Icons with the same text (i.e.
                # "Forward", "Backward", "Turn Left", "Turn Right")
                # that would otherwise override each other.
                self.add(tmp_log, key=index)

                if horizontal:
                    # Make the next Icon appear right of the current one.
                    location = (location[0] + icon_size[0], location[1])
                else:
                    # Make the next Icon appear below the current one.
                    location = (location[0], location[1] + icon_size[1])
