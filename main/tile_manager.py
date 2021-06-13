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
        
        self.tiles_to_draw_x=[-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]
        self.tiles_to_draw_y=[-4,-3,-2,-1,0,1,2,3,4]
        self.tiles_to_draw=np.vstack(map(np.ravel,np.meshgrid(self.tiles_to_draw_x, self.tiles_to_draw_y))).T
            
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
            
    def draw(self):
        x,y=self.get_tile_coords(self.game.camera.x,self.game.camera.y)
        for xy in self.tiles_to_draw:
                obj=self.tile_info.get(xy[0]+x,{}).get(xy[1]+y,{}).get('obj')
                obj.draw()
                
