import pygame
import numpy as np

class screen():
    def __init__(self, game, width, height):
        self.game=game
        self.width=width
        self.height=height
        
    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode([self.width, self.height])
        
    def update(self):
        self.screen.fill((0,0,0))
        
        for tile in self.game.tiles:
            tile.draw()
        
        sorted_index=np.argsort([ent.zorder if hasattr(ent,"zorder") else -9999 for ent in self.game.entities])
        sorted_entities=[self.game.entities[index] for index in sorted_index]
        
        
        for ent in sorted_entities:
            if hasattr(ent,"draw") and (not hasattr(ent,"is_hidden") or not ent.is_hidden):
                ent.draw()
                
        for ent in self.game.lights:
            if hasattr(ent,"draw") and (not hasattr(ent,"is_hidden") or not ent.is_hidden):
                ent.draw()
                
        self.game.cycle.draw()
    
        pygame.display.flip()
