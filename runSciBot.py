from src.GameWindow import *
import sys
import threading

#pygame.init()

gameWindow = GameWindow(8,5)

#thr = threading.Thread(target=gameWindow.updateLoop(), args=(), kwargs={})
#thr.daemon = True
#thr.start() # will run "updateLoop forever 

gameWindow.start()
gameWindow.startInstance()

#pygame.quit()
#sys.exit()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()


#x = BeeBot()

print("we got here")



