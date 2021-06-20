import pygame
import numpy as np

class interaction():
    def __init__(self,game, parent, radius=30, max_anim_frame=60):
        self.game=game
        self.parent=parent
        self.anim_frame=0
        self.radius=radius
        self.radius_sq=self.radius*self.radius
        self.max_anim_frame=max_anim_frame
        self.interaction_components={'worker':'workable', 'eater':'edible', 'toggler':'toggleable'}
        
    def get_closest_interaction(self):
        dmin=999999
        interaction_ent=None
        for ent in self.game.entities:
            if hasattr(ent,'components'):
                for component in self.interaction_components:
                    
                if ent==self:
                    continue
                dx=self.parent.x-ent.x
                dy=self.parent.y-ent.y
                dr=dx*dx+dy*dy
                if dr < dmin and dr < self.work_radius_sq:
                    dmin=dr
                    workable_ent=ent
    
            
