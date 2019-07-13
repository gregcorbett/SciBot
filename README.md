# SciBot
[![Build Status](https://travis-ci.org/stfc/SciBot.svg?branch=develop)](https://travis-ci.org/stfc/SciBot)
[![Coverage Status](https://coveralls.io/repos/github/stfc/SciBot/badge.svg?branch=develop)](https://coveralls.io/github/stfc/SciBot?branch=develop)

contact: scibot-dev@googlegroups.com

## Users
The primary method to run SciBot is via the `runSciBot.exe`.

1. Go to https://github.com/stfc/SciBot/releases/latest
2. Download `runSciBot.exe` and `scenarios.zip` into the same place
3. Unzip `scenarios.zip`
4. Run `runSciBot.exe` (by double clicking it.)

## Developers
If you wish to develop for SciBot, clone the repository and create a feature branch off of develop. Once your feature is ready, make a Pull Request back into develop. SciBot is written in Python 3, hence you will need to install the Python interpreter first. We recommend using [Python 3.6](https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe).

### Requirements for developing, testing and building SciBot
To install SciBot's requirements, run the following command:
```
pip install -r requirements.txt
```

### Building the runSciBot.exe file
If you wish to build a new `runSciBot.exe` file, run the following command:
```
pyinstaller --windowed -F runSciBot.py
```

## Image Sources
SciBot image sourced from: https://www.tes.co.uk/teaching-resource/bee-bot-sequence-powerpoint-6415227

## A note about version numbers
SciBot tries to use [semantic versioning](https://semver.org) with respect to the API exposed to the user by the scenario class/files.
This means that for any given major version of the SciBot executable, all previous scenario files (that share the same major version) should continue to work as they did when the scenario file was created.

As a result of this, we consider a breaking API change to be a change that prevents an older scenario file (that shares the current major version) from working as expected with the next release of SciBot. If such a change is merged, the next release would be the next major version.

Changes that are not exposed to the user by the scenario class/files will not be considered breaking API changes.
