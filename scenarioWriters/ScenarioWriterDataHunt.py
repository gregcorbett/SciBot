"""This file writes a new scibot file."""

from src.Scenario import Scenario
from src.BeeBot import Heading


def main():
    """Write a scibot file."""
    # Initalises a new scenario object and sets the scenario name.
    scenario = Scenario("DataHunt")

    # Tthe size of an individual square
    scenario.set_board_step(100)

    # Sets the width of the map in terms of squares
    scenario.set_logical_width(5)
    # Sets the height of the map in terms of squares
    scenario.set_logical_height(7)

    # Sets the bee bot starting square (x, y)
    scenario.set_beebot_start_position(0, 6)

    # Set the beebot sprite
    scenario.set_beebot_sprite("./img/DataHunt/robot.png")
    # Sets the beebots starting direction, where "UP" is "Heading.NORTH",
    scenario.set_beebot_heading(Heading.NORTH)

    # Sets the image on the map
    scenario.set_background("./img/DataHunt/background.jpg")

    # Add Obastacles
    scenario.add_obstacle(0, 5)
    scenario.add_obstacle(0, 4)
    scenario.add_obstacle(0, 3)
    scenario.add_obstacle(1, 4)
    scenario.add_obstacle(4, 5)
    scenario.add_obstacle(4, 4)
    scenario.add_obstacle(4, 3)
    scenario.add_obstacle(3, 5)
    scenario.add_obstacle(1, 0)
    scenario.add_obstacle(2, 2)

    # Adds goals
    scenario.add_goal(1, 6)
    scenario.add_goal(1, 5)
    scenario.add_goal(2, 5)
    scenario.add_goal(2, 4)
    scenario.add_goal(2, 3)
    scenario.add_goal(1, 3)
    scenario.add_goal(3, 1)
    scenario.add_goal(3, 3)
    scenario.add_goal(3, 4)
    # This one is deliberately repeated, space must be gone to twice
    scenario.add_goal(2, 4)
    # This one is deliberately repeated, space must be gone to twice
    scenario.add_goal(2, 5)
    scenario.add_goal(2, 6)
    scenario.add_goal(3, 6)
    scenario.add_goal(4, 6)
    # This method means the goals must be met in the order added
    scenario.set_ordered_goals(True)

    # Sets the sprite to be displayed when the robot crashes
    scenario.set_beebot_fail_sprite("./img/DataHunt/robotx.png")

    # Copy the LICENSE from below into the Scenario
    scenario.set_license(LICENSE)

    # Writes the scibot file
    scenario.write_to_file()

# Alter this to credit image sources
LICENSE = """
                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc., <http://fsf.org/>
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

 The full version of this license can be found here.
 https://github.com/stfc/SciBot/blob/master/LICENSE

 BeeBot image source.
 https://www.tes.co.uk/teaching-resource/bee-bot-sequence-powerpoint-6415227

 Additonal image sources:
 Wire image
 http://freebie.photography/background/slides/wires.htm

 Arduino image
 https://upload.wikimedia.org/wikipedia/commons/d/d9/Arduino_ftdi_chip-1.jpg

 Keyboard image
 https://upload.wikimedia.org/wikipedia/commons/0/02/OLED_keyboard.jpg

 Rasberry Pi image
 By Lucasbosch - Own work, CC BY-SA 3.0,
 https://commons.wikimedia.org/w/index.php?curid=34179985

 Folder image
 https://commons.wikimedia.org/wiki/File:Blue_folder_seth_yastrov_01.svg

 TV image
 https://upload.wikimedia.org/wikipedia/commons/3/38/TV-icon.png

 Fedora image
 By Macic7 - My computer, GPL,
 https://commons.wikimedia.org/w/index.php?curid=5388618
"""

if __name__ == "__main__":
    main()
