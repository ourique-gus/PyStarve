import pygame
import numpy as np

class camera():
    def __init__(self,game,x, y):
        self.game=game
        self.x=x
        self.y=y
        
    def update(self):
        self.x=self.game.player.x
        self.y=self.game.player.y
