from pico2d import *
import game_framework
import time
from random import*

PIXEL_PER_METER = (10.0 / 0.6) # 10 pixel 30 cm

# Run Speed
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class MonsterState:
    def enter(monster, event):
        pass

    def exit(monster, event):
        pass

    def do(monster):
        monster.dir=0

        if monster.dir==1:
            monster.x += RUN_SPEED_PPS
            if monster.x>500:
                monster.x -= RUN_SPEED_PPS
                monster.dir==0

        elif monster.dir==0:
            monster.x-=RUN_SPEED_PPS
            if monster.x<200:
                monster.x+=RUN_SPEED_PPS
                monster.dir == 1


        monster.frame = (mario.frame+FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time)%2

    def draw(monster):
        if mario.dir == 1:
            mario.Mushroom.clip_draw(int(monster.frame) * 33, 0, 33, 16, monster.x, monster.y)
        else:
            mario.Mushroom.clip_draw(int(monster.frame) * 33, 0, 33, 16, monster.x, monster.y)



class Monster:

    def __init__(self):
        self.x, self.y =800/2, 90
        self.dir =0
        self.frame=0
        self.velocity = 0
        self.event_que=[]
        self.cur_state = MonsterState
        self.cur_state.enter(self,None)  # 현재 상태를 idlestate로 설정
        self.Mushroom = load_image('MushRoom.png')


    def change_state(self,  state):
        # fill here
        pass


    def add_event(self, event):
        self.event_que.insert(0,event)



    def update(self):
        self.cur_state.do(self)
        if len(self.event_que)>0:
            event = self.event_que.pop()
            self.cur_state.exit(self,event)
            self.cur_state=next_state_table[self.cur_state][event]
            self.cur_state.enter(self,event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type,event.key) in key_event_table:
            key_event = key_event_table[(event.type,event.key)]
            self.add_event(key_event)



