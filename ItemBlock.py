
from pico2d import *

import Server
import game_framework
from random import randint
from MapClass import Stage1

class ItemBlock:
    ITEMBlockimage=None

    def __init__(self):
        if ItemBlock.ITEMBlockimage==None:
            ItemBlock.ITEMBlockimage = load_image('ItemBlock.png')
        Server.x=randint(0, Server.ground.w)
        self.x,self.y=Server.x,200
        self.font = load_font('ENCR10B.TTF', 16)
        self.frame=0

    def update(self):
      self.frame = (self.frame+0.3) % 3
      pass


    def get_bb(self):
        return self.x-20,self.y-15,self.x+20,self.y+15

    def draw(self):
            self.ITEMBlockimage.clip_draw(int(self.frame) * 16, 0, 16, 16, self.x, self.y)
