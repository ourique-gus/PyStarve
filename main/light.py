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
        self.sprite=pygame.Surface((2*self.r, 2*self.r), pygame.SRCALPHA)
        self.sprite.fill((0,0,0,0))
        dalpha=255/self.n
        dr=self.r/self.n
        for i in range(self.n):
            pygame.draw.circle(self.sprite,(0,0,0,i*dalpha), (self.r,self.r), self.r-i*dr )
        
    def update(self):
        pass

        
    def draw(self):
        dalpha=255/self.n
        dr=self.r/self.n
        self.game.cycle.sprite.blit(self.sprite,
                (self.x-(self.game.camera.x-self.game.screen.width/2)-self.r, 
                 self.y-(self.game.camera.y-self.game.screen.height/2)-self.r),
            special_flags=pygame.BLEND_RGBA_SUB
            )
        #for i in range(self.n):
        #    pygame.draw.circle(self.game.cycle.sprite, (0,0,0,int(255-i*dalpha), special_flags=pygame.BLEND_RGBA_SUB), 
        #            (self.x-(self.game.camera.x-self.game.screen.width/2),
        #             self.y-(self.game.camera.y-self.game.screen.height/2)
        #            ),
        #            self.r-i*dr)
