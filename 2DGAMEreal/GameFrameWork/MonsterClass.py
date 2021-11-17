from pico2d import *
import game_framework
import time
from random import*

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm

# Run Speed
RUN_SPEED_KMPH = 1.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

# class MonsterState:
#     def __init__(monster):
#         monster.dir =0
#
#
#     def enter(monster, event):
#         pass
#
#     def exit(monster, event):
#         pass
#
#     def do(monster):
#         if monster.dir==0:
#             monster.x+=RUN_SPEED_PPS
#             if monster.x>500:
#                 monster.x -= RUN_SPEED_PPS
#                 monster.dir=1
#         if monster.dir == 1:
#             monster.x -= RUN_SPEED_PPS
#             if monster.x <300:
#                 monster.x += RUN_SPEED_PPS
#                 monster.dir = 0
#         monster.frame = (monster.frame+FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time)%2
#
#
#     def draw(monster):
#         if monster.dir==1:
#             monster.Mushroom.clip_draw(int(monster.frame) * 16, 0, 15, 16, monster.x, monster.y)
#         elif monster.dir==0:
#             monster.Mushroom.clip_draw(int(monster.frame) * 16, 0, 15, 16, monster.x, monster.y)
#
#
#
# class Monster:
#
#     def __init__(self):
#         self.x, self.y =800/2, 80
#         self.dir =0
#         self.frame=0
#         self.velocity = 0
#         self.event_que=[]
#         self.cur_state = MonsterState
#         self.cur_state.enter(self,None)  # 현재 상태를 idlestate로 설정
#         self.Mushroom = load_image('MushRoom.png')
#
#
#     def change_state(self,  state):
#         # fill here
#         pass
#
#
#     def add_event(self, event):
#         self.event_que.insert(0,event)
#
#     def get_bb(self):
#         return self.x - 20, self.y - 18, self.x + 20, self.y + 18
#
#     def update(self):
#         self.cur_state.do(self)
#
#     def draw(self):
#         self.cur_state.draw(self)


class Monster:
    Mushroom=None
    def __init__(self,x=0,y=80,velocity=1):
        if Monster.Mushroom==None:
            Monster.Mushroom = load_image('MushRoom.png')
        self.x,self.y,self.velocity=x,y,velocity
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir=0
        self.frame=0
    def update(self):
        if self.dir == 0:
            self.x+=RUN_SPEED_PPS
            if self.x>400:
                self.x -= RUN_SPEED_PPS
                self.dir=1
        if self.dir == 1:
            self.x -= RUN_SPEED_PPS
            if self.x <0:
                self.x += RUN_SPEED_PPS
                self.dir = 0
        self.frame = (self.frame+FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time)%2


    def get_bb(self):
        return self.x-20,self.y-15,self.x+20,self.y+15

    def draw(self):
        if self.dir == 1:
            self.Mushroom.clip_draw(int(self.frame) * 16, 0, 15, 16, self.x, self.y)
        elif self.dir==0:
            self.Mushroom.clip_draw(int(self.frame) * 16, 0, 15, 16, self.x, self.y)
        draw_rectangle(*self.get_bb())


