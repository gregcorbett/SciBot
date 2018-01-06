# SciBot
[![Build Status](https://travis-ci.org/stfc/SciBot.svg?branch=develop)](https://travis-ci.org/stfc/SciBot)
[![Coverage Status](https://coveralls.io/repos/github/stfc/SciBot/badge.svg?branch=develop)](https://coveralls.io/github/stfc/SciBot?branch=develop)

contact: scibot-dev@googlegroups.com

## Users
1. Go to https://github.com/stfc/SciBot/releases/latest
2. Download runSciBot.exe and scenarios.zip into the same place
3. Unzip scenarios.zip
3. Run the .exe file (by double clicking it.)

## Developers

If you wish to develop for SciBot, clone the repository and create a feature branch off of develop. Once your feature is ready, make a Pull Request back into develop.

### Requirements for building and developing SciBot

Microsoft installers have been linked for each requirement for ease of installation.

1. Python, 3.4 or higher (https://www.python.org/downloads/)
  * exact version used in testing ( https://www.python.org/ftp/python/3.4.3/python-3.4.3.msi)
2. Pygame, 1.9.2 or higher (https://bitbucket.org/pygame/pygame/downloads)
  * exact version used in testing (https://bitbucket.org/pygame/pygame/downloads/pygame-1.9.2a0-hg_ea3b3bb8714a.win32-py3.4.msi)
3. py2exe 0.9.2.2 (https://pypi.python.org/pypi/py2exe/)
  * exact version used in testing (https://pypi.python.org/packages/any/p/py2exe/py2exe-0.9.2.2.win32.exe)

### Building the exe file

After the requirements above are met, open a command line and navigate to the unzipped directory.

Run `python setup.py py2exe`.

## Image Sources
SciBot image sourced from: https://www.tes.co.uk/teaching-resource/bee-bot-sequence-powerpoint-6415227

## A note about version numbers
SciBot tries to use [semantic versioning](https://semver.org) with respect to the API exposed to the user by the scenario class/files.
This means that for any given major version of the SciBot executable, all previous scenario files (that share the same major version) should continue to work as they did when the scenario file was created.

As a result of this, we consider a breaking API change to be a change that prevents an older scenario file (that shares the current major version) from working as expected with the next release of SciBot. If such a change is merged, the next release would be the next major version.

Changes that are not exposed to the user by the scenario class/files will not be considered breaking API changes.
