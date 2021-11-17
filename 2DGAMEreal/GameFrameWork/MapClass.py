from pico2d import *
import game_framework
from MarioClass import Mario



class DrawMap:
    def enter(stage,event):
        pass


    def exit(stage,event):
        pass

    def do(stage):
        stage.x=0.0
        stage.frame = 0
        if mario.x>stage.x:
            stage.x-=0.5

    def draw(stage):
        stage.Stageimage1.clip_draw(stage.frame,100,3447,800,stage.x,105)
        #stage.Stageimage2.clip_draw(stage.frame, 0, 3408, 702, stage.x,100)


class Stage1:

    def __init__(self):
        self.x, self.y = 0,0
        self.Stageimage1 = load_image('stage1.png')
        self.frame=0
        self.event_que=[]
        self.cur_state = DrawMap
        self.cur_state.enter(self,None)  # 현재 상태를 idlestate로 설정



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


class Stage2:

    def __init__(self):
        self.x, self.y = -300, 90
        self.Stageimage2 = load_image('stage2.png')
        self.frame = 0
        self.event_que = []
        self.cur_state = DrawMap
        self.cur_state.enter(self, None)  # 현재 상태를 idlestate로 설정

    def change_state(self, state):
        # fill here
        pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)



