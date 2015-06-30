from src.GameWindow import *
import sys

gameWindow = GameWindow(8,5)
gameWindow.startInstance()
#x = BeeBot()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()