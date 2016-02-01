import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,sprite,start_logical_position_x,start_logical_position_y,step):

        self.logical_position_x = start_logical_position_x
        self.logical_position_y = start_logical_position_y

        self.screen_location_x = start_logical_position_x * step
        self.screen_location_y = start_logical_position_y * step

        self.sprite = sprite

    def display(self,screen):
        if self.sprite != None:
            screen.blit(self.sprite,(self.screen_location_x,self.screen_location_y))
