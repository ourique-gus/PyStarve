import pygame
import numpy as np

class hud():
    def __init__(self,game):
        self.game=game
        self.w=self.game.screen_width
        self.h=self.game.screen_height
        self.sprite=pygame.Surface((50,50))
        
        self.hunger_bar=pygame.Surface((50,100))
        self.hunger_bar.fill((101, 67, 33))
        
        self.health_bar=pygame.Surface((50,100))
        self.health_bar.fill((101, 67, 33))
                        
    def update(self):
        pass
                
    def draw(self):
        if not hasattr(self.game,'player'):
            return
        self.hunger_bar.fill((101, 67, 33))
        self.health_bar.fill((101, 67, 33))

        hunger_meter = self.game.player.components['hunger'].current/self.game.player.components['hunger'].max
        pygame.draw.rect(self.hunger_bar, (255, 0,0), (10,90-80*hunger_meter, 30,80*hunger_meter) )
        
        self.game.screen.screen.blit(self.hunger_bar, (50, 50) )

        health_meter = self.game.player.components['health'].current/self.game.player.components['health'].max
        pygame.draw.rect(self.health_bar, (230, 0,126), (10,90-80*health_meter, 30,80*health_meter) )

        self.game.screen.screen.blit(self.health_bar, (125, 50) )
        
