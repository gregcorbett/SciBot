import os
import sys
#print(os.getcwd()+"\..\scenarios")
#sys.path.append(os.getcwd())
#sys.path.append(os.getcwd()+"\..\scenarios")
#sys.path.append(os.getcwd()+"\..\src")
del os
del sys

from src.GameWindow import *

gameWindow = GameWindow()
gameWindow.chooseScenario()
gameWindow.loadScenario()
gameWindow.startScenario()
