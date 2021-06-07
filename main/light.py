import pygame
import numpy as np

class light():
    def __init__(self,game,x, y, r, n):
        self.game=game
        self.x=x
        self.y=y
        self.r=r
        self.n=n
        self.is_updating=True
        self.is_hidden=False
        
    def update(self):
        pass

        
    def draw(self):
        dalpha=255/self.n
        dr=self.r/self.n
        for i in range(self.n):
            pygame.draw.circle(self.game.cycle.sprite, (0,0,0,int(255-i*dalpha)), 
                    (self.x-(self.game.camera.x-self.game.screen.width/2),
                     self.y-(self.game.camera.y-self.game.screen.height/2)
                    ),
                    self.r-i*dr)
