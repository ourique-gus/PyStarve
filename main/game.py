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
from main.prefabs.evergreen import evergreen as prefabs_evergreen
from main.prefabs.tomato import tomato as prefabs_tomato
from main.hud import hud


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
        self.cycle=cycle(self,60*60, 0.7)
        self.hud=hud(self)
        
        
        self.camera=camera(self,0,0)
        
        self.tiles=[]
        self.entities=[]
        self.lights=[]
        
        print("Game started")
        
        for i in range(-30,30):
            for j in range(-30,30):
                kind=i*i+j*j < 20 and 'forest' or 'water'
                self.tiles.append( tile(self, i,j, kind ) )

                
        self.entities.append(self.player)
        for i in range(20):
            r=np.random.uniform(0,400)
            theta=np.random.uniform(0,2*np.pi)
            x=r*np.cos(theta)
            y=r*np.sin(theta)
            self.entities.append(prefabs_evergreen(self,10,10, x,y))
            
        self.entities.append(prefabs_tomato(self,10,10, 150,150))
        
        self.lights.append(light(self,0,100,100,100))
        self.lights.append(light(self,700,500,100,100))
        self.lights.append(light(self,500,700,100,100))
        
        self.non_removed_entities=[]
        
        while self.is_running:
            #print(self.clock. get_fps())
            self.clock.tick(self.tps)
    
            self.controls.get_keys()
            
            self.non_removed_entities=[]
            for ent in self.entities:
                if not (hasattr(ent,'remove') and ent.remove==True):
                    self.non_removed_entities.append(ent)
                else:
                    if hasattr(ent,'on_remove'):
                        ent.on_remove()
            self.entities=self.non_removed_entities
                    
            
            for ent in self.entities:
                if hasattr(ent,"update") and hasattr(ent,"is_updating") and ent.is_updating:
                    ent.update()
                    
                    if hasattr(ent, 'components'):
                        for component in ent.components:
                            if hasattr(ent.components[component], 'update'):
                                ent.components[component].update()
                    
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
                    
                

