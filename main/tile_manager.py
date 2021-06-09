import pygame
import numpy as np

class tile_manager():
    def __init__(self,game):
        self.game=game
        self.size=100
        self.tile_dict={
            'forest':{'colour':(0,150,0), 'collision':False},
            'orange':{'colour':(150,150,0), 'collision':False},
            'water':{'colour':(0,0,150), 'collision':True},
            }
        self.tile_info={}
            
    def start(self):
        self.tile_sprites={i:pygame.Surface((self.size,self.size)) for i in self.tile_dict}
        for i in self.tile_dict:
            self.tile_sprites[i].fill(self.tile_dict[i]['colour'])
            
    def get_tile_coords(self, x,y):
        return int(np.rint(x/self.game.tile_manager.size)),int(np.rint(y/self.game.tile_manager.size))
            
    def collider_tiles(self):
        self.tile_collider=[]
        xy_tiles=np.array([[tile.x, tile.y] for tile in self.game.tiles])
        for tile in self.game.tiles:
            dx=tile.x-xy_tiles[:,0]
            dy=tile.y-xy_tiles[:,1]
            

