import pygame
import numpy as np

class player():
    def __init__(self,game,width,height,x0,y0):
        self.game=game
        self.width=width
        self.height=height
        self.x=x0
        self.y=y0
        self.is_updating=True
        self.is_hidden=False
        self.sprite=pygame.image.load("sprite/player/wilson.png")
        self.size=self.sprite.get_size()
        self.speed=5
        self.zorder=0
        
    def update(self):
        dx=-self.game.controls.keys[pygame.K_a]+self.game.controls.keys[pygame.K_d]
        dy=-self.game.controls.keys[pygame.K_w]+self.game.controls.keys[pygame.K_s]
        
        r=np.sqrt(dx*dx+dy*dy)
        
        if r > 0:
            dx/=r
            dy/=r
            print(dx, dy)
            self.x+=self.speed*dx
            self.y+=self.speed*dy
        
    def draw(self):
        self.game.screen.screen.blit(self.sprite,
                    (self.x-self.size[0]/2-(self.game.camera.x-self.game.screen.width/2),
                     self.y-self.size[1]/2-(self.game.camera.y-self.game.screen.height/2)
                    )
                )
        
