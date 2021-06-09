import pygame
import numpy as np

class tile():
    def __init__(self,game,x, y, kind):
        self.game=game
        self.size=self.game.tile_manager.size
        self.x_id=x
        self.y_id=y
        self.x=x*self.size
        self.y=y*self.size
        self.kind=kind
        self.sprite=self.game.tile_manager.tile_sprites[kind]
        self.collision=self.game.tile_manager.tile_dict[kind]['collision']
        self.max_dist=900*900
        
        if not self.x_id in self.game.tile_manager.tile_info:
            self.game.tile_manager.tile_info[self.x_id]={}
        self.game.tile_manager.tile_info[self.x_id][self.y_id]={'kind':self.kind, 'collision':self.collision}
        
    def draw(self):
        dx=self.x-self.game.camera.x
        dy=self.y-self.game.camera.y
        dr=dx*dx+dy*dy
        if dr < self.max_dist:
            self.game.screen.screen.blit(self.sprite,
                        (self.x-self.game.tile_manager.size/2-(self.game.camera.x-self.game.screen.width/2),
                         self.y-self.game.tile_manager.size/2-(self.game.camera.y-self.game.screen.height/2)
                        )
                    )
