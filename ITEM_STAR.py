from pico2d import *

import Server

import game_framework
from random import randint

class ItemStar:
    ItemStarimage=None
    def __init__(self):
        if ItemStar.ItemStarimage==None:
            ItemStar.ItemStarimage = load_image('ITEM-STAR.png')

        Server.x=randint(0, Server.ground.w)
        self.x=Server.x

        self.y=217
        self.font = load_font('ENCR10B.TTF', 16)
        self.frame=0

    def update(self):
        self.frame = (self.frame+0.3) % 3


    def get_bb(self):
        return self.x-20,self.y-15,self.x+20,self.y+15

    def draw(self):
        self.ItemStarimage.clip_draw(int(self.frame) * 16, 0, 16, 16, self.x, self.y)
