from enum import IntEnum
import pygame

class CustomEvent(IntEnum):
	MOVE_BEEBOT_UP = pygame.USEREVENT+1
	MOVE_BEEBOT_LEFT = pygame.USEREVENT+2
	MOVE_BEEBOT_DOWN = pygame.USEREVENT+3
	MOVE_BEEBOT_RIGHT = pygame.USEREVENT+4
	
	RUN_FAIL = pygame.USEREVENT+5
	RUN_WIN = pygame.USEREVENT+6
	
	
