import pygame

class Goal(pygame.sprite.Sprite):
    def __init__(self,sprite,startLogicalPositionX,startLogicalPositionY,step):
        
        self.logicalPositionX = startLogicalPositionX
        self.logicalPositionY = startLogicalPositionY
        
        self.screenLocationX = startLogicalPositionX * step
        self.screenLocationY = startLogicalPositionY * step
        
        self.sprite = sprite

    def display(self,screen):
        if self.sprite != None:
            screen.blit(self.sprite,(self.screenLocationX,self.screenLocationY))