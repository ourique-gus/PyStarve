import pygame
import numpy as np

class controls():
    def __init__(self,game):
        self.game=game
        self.keys={}
        
    def get_keys(self):
        self.keys=pygame.key.get_pressed()
