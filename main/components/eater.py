import pygame
import numpy as np

class eater():
    def __init__(self,game, parent):
        self.game=game
        self.parent=parent
        self.tick=0
        self.delay=60
        self.eat_radius=30
        self.eat_radius_sq=self.eat_radius*self.eat_radius
        
    def eat(self, target):
        if 'edible' in target.components:
            target.components['edible'].on_eat(self.parent)
            
    def find_entity_to_eat(self):
        dmin=999999
        edible_ent=None
        for ent in self.game.entities:
            if hasattr(ent,'components') and 'edible' in ent.components:
                if ent==self:
                    continue
                dx=self.parent.x-ent.x
                dy=self.parent.y-ent.y
                dr=dx*dx+dy*dy
                if dr < dmin and dr < self.eat_radius_sq:
                    dmin=dr
                    edible_ent=ent
        return edible_ent
            
    def eat_nearest_entity(self):
        if self.tick > 0:
            return
        edible_entity = self.find_entity_to_eat()
        if edible_entity:
            self.tick=self.delay
            self.eat(edible_entity)
        
    def update(self):
        if self.tick > 0:
            self.tick-=1
