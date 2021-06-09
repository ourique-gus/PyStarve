import pygame
import numpy as np
from main.screen import screen
from main.controls import controls
from main.player import player
from main.cycle import cycle
from main.light import light
from main.camera import camera
from main.tile import tile
from main.tile_manager import tile_manager


class game():
    
    def __init__(self):
        self.is_running=False
        
        self.start_screen(1366, 768)
        self.start_clock(60)
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
        self.tick=0

        self.tile_manager=tile_manager(self)
        self.tile_manager.start()
        
        self.controls=controls(self)
        self.player=player(self,20,20,50,50)
        self.cycle=cycle(self,180)
        
        
        self.camera=camera(self,0,0)
        
        self.tiles=[]
        self.entities=[]
        self.lights=[]
        
        for i in range(-20,20):
            for j in range(-20,20):
                kind=i*i+j*j < 20 and 'forest' or 'water'
                self.tiles.append( tile(self, i,j, kind ) )

                
        print("AAAAAAAAAAAAAAAAAAAA", len(self.tiles))
                
        self.entities.append(self.player)
        
        self.lights.append(light(self,500,500,100,100))
        self.lights.append(light(self,700,500,100,100))
        self.lights.append(light(self,500,700,100,100))
        
        while self.is_running:
            print(self.clock. get_fps())
            self.clock.tick(self.tps)
    
            self.controls.get_keys()
            
            for ent in self.entities:
                if hasattr(ent,"update") and hasattr(ent,"is_updating") and ent.is_updating:
                    ent.update()
                    
            self.cycle.update()
                    
            for ent in self.lights:
                if hasattr(ent,"update") and hasattr(ent,"is_updating") and ent.is_updating:
                    ent.update()
                    
            self.camera.update()
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                                   
            self.screen.update()
            
            self.tick+=1
                    
                

