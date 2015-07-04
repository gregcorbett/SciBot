from src.GameWindow import *
import sys
import threading

class updater:
	def run():
		
		print("BOO")
		
		clock = pygame.time.Clock() 
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			
				clock.tick(30)
				pygame.display.update()

thr = threading.Thread(target=updater, args=(), kwargs={})
thr.start() # will run "updateLoop forever 

gameWindow = GameWindow(8,5)
gameWindow.startInstance()
#x = BeeBot()

print("we got here")



