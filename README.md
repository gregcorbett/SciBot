# SciBot
[![Build Status](https://travis-ci.org/stfc/SciBot.svg?branch=develop)](https://travis-ci.org/stfc/SciBot)
[![Coverage Status](https://coveralls.io/repos/github/stfc/SciBot/badge.svg?branch=develop)](https://coveralls.io/github/stfc/SciBot?branch=develop)

contact: scibot-dev@googlegroups.com

## Users
1. Go to https://github.com/gregcorbett/SciBot/releases/latest
2. Download runSciBot.exe and scenarios.zip into the same place
3. Unzip scenarios.zip
3. Run the .exe file (by double clicking it.)

## Developers

Download the soucre.zip, unzip it and navigate to the source code directory

### Requirements for building and developing SciBot

Microsoft installers have been linked for each requirement for easy of installation.

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
