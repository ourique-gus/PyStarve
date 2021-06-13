import pygame
import numpy as np

class collider():
    def __init__(self,game, parent):
        self.game=game
        self.parent=parent
        self.tile_scale=0.998
        self.tile_size=self.tile_scale*self.game.tile_manager.size
            
    def get_collision(self):
        x_tile,y_tile=self.game.tile_manager.get_tile_coords(self.parent.x,self.parent.y)
        for xy in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
            collision = self.game.tile_manager.tile_info.get(x_tile+xy[0],{}).get(y_tile+xy[1],{}).get('collision')
            if collision:
                tile_x=(x_tile+xy[0])*self.tile_size
                tile_y=(y_tile+xy[1])*self.tile_size
                xl=(self.parent.x-self.parent.width/2)-(tile_x+self.tile_size/2)
                xr=-(self.parent.x+self.parent.width/2)+(tile_x-self.tile_size/2)
                yt=(self.parent.y-self.parent.width/2)-(tile_y+self.tile_size/2)
                yb=-(self.parent.y+self.parent.width/2)+(tile_y-self.tile_size/2)
                dx=max([xl,xr])
                dy=max([yt,yb])
                if dx < 0 and dy < 0:
                    if dx > dy:
                        sign=xl < xr and -1 or 1
                        self.parent.x-=dx*sign
                    else:
                        sign=yt < yb and -1 or 1
                        self.parent.y-=dy*sign
