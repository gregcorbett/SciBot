import os
import sys
sys.path.append(os.getcwd())
del os
del sys

from src.GameWindow import *

gameWindow = GameWindow()
gameWindow.chooseScenario()
gameWindow.loadScenario()
gameWindow.startScenario()