import pygame
import numpy as np
from main.screen import screen
from main.controls import controls
from main.player import player
from main.cycle import cycle


class game():
    
    def __init__(self):
        self.is_running=False
        
        self.start_screen(1366, 768)
        self.start_clock(30)
        self.start_game()
        
        
        
        
    def start_screen(self,width, height):
        self.screen_width=width
        self.screen_height=height
        self.screen=screen(self,self.screen_width, self.screen_height)
        self.screen.start()
        
    def start_clock(self,tps):
        self.clock = pygame.time.Clock()
        self.tps=tps
    
    def start_game(self):
        self.is_running=True
        
        self.controls=controls(self)
        self.player=player(self,10,10,10,10)
        self.cycle=cycle(self,60)
        
        self.entities=[]
        
        self.entities.append(self.cycle)
        self.entities.append(self.player)
        
        while self.is_running:
            self.clock.tick(self.tps)
    
            self.controls.get_keys()
            
            for ent in self.entities:
                if hasattr(ent,"update") and hasattr(ent,"is_updating") and ent.is_updating:
                    ent.update()
    
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                                   
            self.screen.update()
                    
                

