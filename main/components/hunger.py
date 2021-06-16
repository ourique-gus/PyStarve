import pygame
import numpy as np

class hunger():
    def __init__(self,game, parent, max_hunger=100, rate=10):
        self.game=game
        self.parent=parent
        self.max=max_hunger
        self.current=self.max
        self.rate=rate
        
    def do_delta(self,value):
        self.current+=value
        if self.current < 0:
            self.current=0
        if self.current > self.max:
            self.current=self.max
        
    def update(self):
        self.do_delta(-self.rate/self.game.tps)
