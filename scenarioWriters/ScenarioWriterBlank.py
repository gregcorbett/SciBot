"""This file writes a new scibot file."""

from src.Scenario import Scenario
from src.BeeBot import Heading


def main():
    """Write a scibot file."""
    # Add commands below

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
