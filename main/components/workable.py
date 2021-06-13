import pygame
import numpy as np

class workable():
    def __init__(self,game, parent, num_work=10):
        self.game=game
        self.parent=parent
        self.num_work=num_work
        self.max_num_work=num_work
        self.anim_frame=0
        self.max_anim_frame=30
        
    def set_num_work(self,num_work):
        self.num_work=num_work
        self.max_num_workd=num_work

    def worked(self, worker, work_num=1):
        self.num_work-=work_num
        print(self.num_work)
        if self.num_work <= 0:
            self.work_done(worker)
        else:
            self.work_callback(worker)
            
    def work_done(self,worker):
        self.parent.remove=True
        
    def work_callback(self,worker):
        self.anim_frame=self.max_anim_frame
        self.x0=self.parent.x
        self.y0=self.parent.y
        print("TOMATE")
        
    def update(self):
        if self.anim_frame > 1:
            print("here")
            self.anim_frame-=1
            self.parent.x=self.x0+np.random.uniform(-5,5)
            self.parent.y=self.y0+np.random.uniform(-5,5)
        if self.anim_frame==1:
            self.parent.x=self.x0
            self.parent.y=self.y0
            
