import pygame
import numpy as np

class worker():
    def __init__(self,game, parent):
        self.game=game
        self.parent=parent
        self.tick=0
        self.delay=60
        self.work_radius=30
        self.work_radius_sq=self.work_radius*self.work_radius
        
    def work(self, target, work_num=1):
        if 'workable' in target.components:
            target.components['workable'].worked(self.parent, work_num)
            
    def find_entity_to_work(self):
        dmin=999999
        workable_ent=None
        for ent in self.game.entities:
            if hasattr(ent,'components') and 'workable' in ent.components:
                if ent==self:
                    continue
                dx=self.parent.x-ent.x
                dy=self.parent.y-ent.y
                dr=dx*dx+dy*dy
                if dr < dmin and dr < self.work_radius_sq:
                    dmin=dr
                    workable_ent=ent
        return workable_ent
            
    def work_on_nearest_entity(self):
        if self.tick > 0:
            return
        workable_entity = self.find_entity_to_work()
        if workable_entity:
            self.tick=self.delay
            workable_entity.components['workable'].worked(self.parent,1)
        
    def update(self):
        if self.tick > 0:
            self.tick-=1
