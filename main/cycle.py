import pygame
import numpy as np

class cycle():
    def __init__(self,game,duration):
        self.game=game
        self.duration=duration
        self.current_time=0

        self.is_updating=True
        self.is_hidden=False
        self.sprite=pygame.Surface((self.game.screen.width, self.game.screen.height), pygame.SRCALPHA)
        self.hole=pygame.Surface((100,100), pygame.SRCALPHA)
        self.sprite.fill((0,0,0))
        self.hole.fill((0,0,0,255))
        self.zorder=1
        
    def update(self):
        self.sprite.fill((0,0,0))
        self.current_time+=1
        if self.current_time >= self.duration:
            self.current_time=0
        self.alpha=int(255*self.current_time/self.duration)
        self.sprite.set_alpha(self.alpha)
        
        self.sprite.blit(self.hole,(self.game.player.x-50,self.game.player.y-50), special_flags=pygame.BLEND_RGBA_SUB)
        
        
        
    def draw(self):
        self.game.screen.screen.blit(self.sprite, (0,0))
