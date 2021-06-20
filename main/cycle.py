import pygame
import numpy as np

class cycle():
    def __init__(self,game,duration, day_night_ratio=0.5):
        self.game=game
        self.duration=duration
        self.current_time=0
        self.day_night_ratio=day_night_ratio
        
        self.transition_ratio=0.05

        self.is_updating=True
        self.is_hidden=False
        self.sprite=pygame.Surface((self.game.screen.width, self.game.screen.height), pygame.SRCALPHA)
        
        self.alpha_time=np.array([
                    [0, 0.5],#0],
                    [self.day_night_ratio-self.transition_ratio/2, 1],#0],
                    [self.day_night_ratio+self.transition_ratio/2, 1],
                    [1-self.transition_ratio,1],
                    [1,1]#0]
                    ])
        print(self.alpha_time)
        
        self.hole=pygame.Surface((100,100), pygame.SRCALPHA)
        self.sprite.fill((0,0,0))
        self.hole.fill((0,0,0,0))
        #pygame.draw.circle(self.hole,(255,0,0,255),(50,50),50)
        self.zorder=1
        
    def update(self):
        self.sprite.fill((0,0,0))
        self.current_time+=1
        if self.current_time >= self.duration:
            self.current_time=0
        self.alpha=self.get_alpha()
        #self.alpha=100
        self.sprite.set_alpha(self.alpha)
        
    def get_alpha(self):
        day_frac=float(self.current_time)/self.duration
        return int(np.interp(day_frac,self.alpha_time[:,0], self.alpha_time[:,1])*255)
        
    def draw(self):
        self.game.screen.screen.blit(self.sprite, (0,0))
