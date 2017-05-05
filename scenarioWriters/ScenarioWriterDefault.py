"""This file writes a new scibot file."""

from src.Scenario import Scenario
from src.BeeBot import Heading


def main():
    """Write a scibot file."""
    # Initalises a new scenario object and sets the scenario name.
    scenario = Scenario("Default")

    # Tthe size of an individual square
    scenario.set_board_step(150)

    # Sets the width of the map in terms of squares
    scenario.set_logical_width(5)
    # Sets the height of the map in terms of squares
    scenario.set_logical_height(8)

    # Sets the bee bot starting square (x, y)
    scenario.set_beebot_start_position(3, 1)

    # Set the beebot sprite
    scenario.set_beebot_sprite("./img/Default/robot.jpg")
    # Sets the beebots starting direction, where "UP" is "Heading.NORTH",
    # other options are Heading.East etc
    scenario.set_beebot_heading(Heading.NORTH)

    # Sets the image on the map
    scenario.set_background("./img/Default/background.jpg")
    # If the image has no grid, one can be added by choosing a (R,G,B) tuple
    scenario.set_border_colour((0, 0, 0))

    # This line addes an obstacle at square (2,1)
    # with sprite "./img/Default/obstacle1.jpg".
    # scenario.addObstacle(2,1) would add an obstacle at (2,1) with no sprite,
    # ie it will show whatever is on the background
    scenario.add_obstacle(2, 1, "./img/Default/obstacle1.jpg")
    # Add another obstacle
    scenario.add_obstacle(2, 3, "./img/Default/obstacle1.jpg")

    # Adds a goal square at (1,2) with sprite "./img/Default/goal1.jpg"
    scenario.add_goal(1, 2, "./img/Default/goal1.jpg")
    # add another goal
    scenario.add_goal(2, 0, "./img/Default/goal1.jpg")

    # This method means the goals must be met in the order added (Default)
    # scenario.set_ordered_goals(True)
    # This method means the goals can be met in any order
    scenario.set_ordered_goals(False)

    # Sets the sprite to be displayed when the robot crashes
    scenario.set_beebot_fail_sprite("./img/Default/robotx.jpg")

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
"""

if __name__ == "__main__":
    main()
