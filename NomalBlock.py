from pico2d import *

import Server
import game_framework
from random import randint
from MapClass import Stage1

class Nomalblock:
    NomalBlockimage=None

    def __init__(self):
        if Nomalblock.NomalBlockimage==None:
            Nomalblock.NomalBlockimage = load_image('NomalBlock.png')
        self.x,self.y=randint(0,Server.ground.w),200
        self.font = load_font('ENCR10B.TTF', 16)
        self.frame=0

    def update(self):
      pass


    def get_bb(self):
        return self.x-20,self.y-15,self.x+20,self.y+15

    def draw(self):
            self.NomalBlockimage.draw(self.x,self.y)
