

from pico2d import *
import game_framework
import time
from random import randint
from MapClass import Stage1
PIXEL_PER_METER = (10.0 / 0.8)

# Run Speed
RUN_SPEED_KMPH = 1.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Mush:
    Mushroom=None
    def __init__(self,x=70,y=75,velocity=1):
        if Mush.Mushroom==None:
            Mush.Mushroom = load_image('MushRoom.png')
        self.x,self.y,self.velocity=randint(50,150),y,velocity
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir=0
        self.frame=0

    def update(self):
        if self.dir == 0:
            self.x+=RUN_SPEED_PPS * randint(1,2)
            if self.x>400:
                self.x -= RUN_SPEED_PPS  * randint(1,2)
                self.dir=1
        if self.dir == 1:
            self.x -= RUN_SPEED_PPS  * randint(1,2)
            if self.x <0:
                self.x += RUN_SPEED_PPS  * randint(1,2)
                self.dir = 0
        self.frame = (self.frame+FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time)%2


    def get_bb(self):
        return self.x-20,self.y-15,self.x+20,self.y+15

    def draw(self):
        if self.dir == 1:
            self.Mushroom.clip_draw(int(self.frame) * 16, 0, 15, 16, self.x, self.y)
        elif self.dir==0:
            self.Mushroom.clip_draw(int(self.frame) * 16, 0, 15, 16, self.x, self.y)




