import pygame
import numpy as np

class edible():
    def __init__(self,game, parent, hunger,health,sanity):
        self.game=game
        self.parent=parent
        self.hunger=hunger
        self.health=health
        self.sanity=sanity
            
    def on_eat(self,eater):
        self.parent.remove=True
        if 'hunger' in eater.components:
            eater.components['hunger'].do_delta(self.hunger)
        if 'health' in eater.components:
            eater.components['health'].do_delta(self.health)
        if 'sanity' in eater.components:
            eater.components['sanity'].do_delta(self.sanity)
        

