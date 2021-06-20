import pygame
import numpy as np

class health():
    def __init__(self,game, parent, max_health=100):
        self.game=game
        self.parent=parent
        self.max=max_health
        self.current=self.max
        
    def do_delta(self,value):
        self.current+=value
        if self.current < 0:
            self.current=0
        if self.current > self.max:
            self.current=self.max
        
    def update(self):
        if 'hunger' in self.parent.components and self.parent.components['hunger'].current <= 0:
            self.do_delta(-0.1)
