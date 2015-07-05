from src.GameWindow import *
import sys
import threading

#pygame.init()

gameWindow = GameWindow(8,5)

#thr = threading.Thread(target=gameWindow.updateLoop(), args=(), kwargs={})
#thr.daemon = True
#thr.start() # will run "updateLoop forever 

#gameWindow.start()
#gameWindow.startInstance()

#pygame.quit()
#sys.exit()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				gameWindow.robot.moveForward(gameWindow.screen)
				
		gameWindow.display()
		pygame.display.update()


#x = BeeBot()

print("we got here")



