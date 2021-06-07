import pygame
import numpy as np

class tile():
    def __init__(self,game,x, y, colour):
        self.game=game
        self.x=x
        self.y=y
        self.colour=colour
        self.size=100
        self.sprite=pygame.Surface((self.size,self.size))
        self.sprite.fill(self.colour)
        
    def draw(self):
        self.game.screen.screen.blit(self.sprite,
                    (self.x-self.size/2-(self.game.camera.x-self.game.screen.width/2),
                     self.y-self.size/2-(self.game.camera.y-self.game.screen.height/2)
                    )
                )
