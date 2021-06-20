import pygame
import numpy as np
from main.components.edible import edible

class tomato():
    def __init__(self,game,width,height,x0,y0):
        self.game=game
        self.width=width
        self.height=height
        self.x=x0
        self.y=y0
        self.is_updating=True
        self.is_hidden=False
        self.sprite=pygame.transform.scale(pygame.image.load("sprite/prefabs/tomato.png"), (35,35))
        self.size=self.sprite.get_size()
        self.zorder=-1
        self.components={'edible':edible(self.game,self, 50,10,0)}
        
    def update(self):
        pass
        
    def draw(self):
        self.game.screen.screen.blit(self.sprite,
                    (self.x-self.size[0]/2-(self.game.camera.x-self.game.screen.width/2),
                     self.y-self.size[1]/2-(self.game.camera.y-self.game.screen.height/2)
                    )
                )
        
    def on_remove(self):
        print("AH QUE PENA")
