import pygame
import numpy as np
from main.light import light
from main.components.toggleable import toggleable

def toggle(parent, toggler):
    if not parent.light:
        parent.light=light(parent.game,parent.x,parent.y, 200, 100)
        parent.game.entities.append(parent.light)
        parent.current_sprite=0
    else:
        parent.light.remove=True
        parent.light=None
        parent.current_sprite=1

class campfire():
    def __init__(self,game,width,height,x0,y0):
        self.game=game
        self.width=width
        self.height=height
        self.x=x0
        self.y=y0
        self.is_updating=True
        self.is_hidden=False
        self.sprite=[   pygame.image.load("sprite/prefabs/campfire/campfire_01.png"),
                        pygame.image.load("sprite/prefabs/campfire/campfire_02.png")
                    ]
        self.size=self.sprite[0].get_size()
        self.zorder=-1
        self.components={'toggleable':toggleable(self.game,self)}
        self.light=None
        self.current_sprite=1
        
        self.components['toggleable'].set_toggle_function(toggle)
        
    def update(self):
        pass
        
    def draw(self):
        self.game.screen.screen.blit(self.sprite[self.current_sprite],
                    (self.x-self.size[0]/2-(self.game.camera.x-self.game.screen.width/2),
                     self.y-self.size[1]/2-(self.game.camera.y-self.game.screen.height/2)
                    )
                )
                
    def update(self):
        pass
        
    def on_remove(self):
        pass
