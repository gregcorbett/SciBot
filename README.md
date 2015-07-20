# SciBot
contact: scibot-dev@googlegroups.com
##To Run

1. Download the zip (https://github.com/gregcorbett/SciBot/archive/master.zip)
2. Extract the zip
3. Open up cmd
4. navigate to unzipped files
5. Either:
  1. run `python runSciBot.py`
    * see requirements section below
  2. double click `runSciBot.exe`

##Image Sources
SciBot image sourced from: https://www.tes.co.uk/teaching-resource/bee-bot-sequence-powerpoint-6415227

##Requirements for building and developing SciBot

Microsoft installers have been linked for each requirement for easy of installation.

1. Python, 3.4 or higher (https://www.python.org/downloads/)
  * exact version used in testing ( https://www.python.org/ftp/python/3.4.3/python-3.4.3.msi)
2. Pygame, 1.9.2 or higher (https://www.python.org/downloads/)
  * exact version used in testing (http://pygame.org/ftp/pygame-1.9.2a0.win32-py3.2.msi)
3. py2exe 0.9.2.2(https://pypi.python.org/pypi/py2exe/)
  * exact version used in testing (https://pypi.python.org/packages/any/p/py2exe/py2exe-0.9.2.2.win32.exe)

##Building the exe file

After the requirements below are met, open a command line and navigate to the unzipped directory.

Run `python build.py py2exe`.