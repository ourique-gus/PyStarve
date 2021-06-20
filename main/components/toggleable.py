import pygame
import numpy as np

class toggleable():
    def __init__(self,game, parent):
        self.game=game
        self.parent=parent
        
    def set_toggle_function(self,function):
        self.toggle_function=function
        
    def toggle(self,toggler):
        print(self.game,self.parent,toggler)
        self.toggle_function(self.parent,toggler)
        
    def update(self):
        pass
