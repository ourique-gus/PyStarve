import pygame
import numpy as np

class toggler():
    def __init__(self,game, parent):
        self.game=game
        self.parent=parent
        self.tick=0
        self.delay=60
        self.toggle_radius=30
        self.toggle_radius_sq=self.toggle_radius*self.toggle_radius
        
    def toggle(self, target, toggle_num=1):
        if 'toggleable' in target.components:
            target.components['toggleable'].toggleed(self.parent, toggle_num)
            
    def find_entity_to_toggle(self):
        dmin=999999
        toggleable_ent=None
        for ent in self.game.entities:
            if hasattr(ent,'components') and 'toggleable' in ent.components:
                if ent==self:
                    continue
                dx=self.parent.x-ent.x
                dy=self.parent.y-ent.y
                dr=dx*dx+dy*dy
                if dr < dmin and dr < self.toggle_radius_sq:
                    dmin=dr
                    toggleable_ent=ent
        return toggleable_ent
            
    def toggle_nearest_entity(self):
        if self.tick > 0:
            return
        toggleable_entity = self.find_entity_to_toggle()
        if toggleable_entity:
            self.tick=self.delay
            toggleable_entity.components['toggleable'].toggle(self.parent)
        
    def update(self):
        if self.tick > 0:
            self.tick-=1
