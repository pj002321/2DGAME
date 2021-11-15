from pico2d import *
import game_framework
import time
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP,LEFT_UP,JUMP_UP,JUMP_DOWN = range(6)
# fill here

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN,SDLK_SPACE): JUMP_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_SPACE): JUMP_UP
}

PIXEL_PER_METER = (10.0 / 0.6) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class IdleState:
    def enter(mario,event):
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.velocity -=RUN_SPEED_PPS
        elif event==LEFT_UP:
            mario.velocity +=RUN_SPEED_PPS
        mario.timer = 1000


    def exit(mario,event):
        pass

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time+1) % 2
        mario.timer -= 1

    def draw(mario):
            mario.Idleimage.clip_draw(int(mario.frame)*40,0,40,53,mario.x,mario.y)

class RunState:
    def enter(mario,event):
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS

        mario.dir= clamp(-1, mario .velocity, 1)

    def exit(mario,event): # Exit Action
        pass

    def do(mario): # Do Activity
        mario.frame = (mario.frame+FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 5
        mario.timer -= 1
        mario.x += mario.velocity*game_framework.frame_time
        mario.x = clamp(25, mario.x, 800 - 25)

    def draw(mario):
        if mario.dir == 1:
            mario.RRunimage.clip_draw(int(mario.frame) * 40, 0, 40, 53, mario.x, mario.y)
        else:
            mario.LRunimage.clip_draw(int(mario.frame) * 40, 0, 40, 53, mario.x, mario.y)

class JumpState:
    def enter(mario,event):
        mario.frame=0

    def exit(mario, event):  # Exit Action
        pass

    def do(mario):
        mario.frame=(mario.frame+FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time)%5
        mario.y += mario.velocity * game_framework.frame_time
    def draw(mario):
        if mario.dir == 1:
            mario.RRunimage.clip_draw(int(mario.frame) * 40, 0, 40, 53, mario.x, mario.y)
        else:
            mario.LRunimage.clip_draw(int(mario.frame) * 40, 0, 40, 53, mario.x, mario.y)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,RIGHT_DOWN: RunState, LEFT_DOWN: RunState,JUMP_DOWN:JumpState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,JUMP_DOWN:JumpState},
    JumpState: {RIGHT_UP: RunState, LEFT_UP: RunState,LEFT_DOWN: RunState, RIGHT_DOWN: RunState,JUMP_UP:IdleState}

}
class Mario:

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.LRunimage = load_image('MarioRunStateLeft.png')
        self.RRunimage = load_image('MarioRunStateRight.png')
        self.Idleimage = load_image('MarioIdleState.png')
        self.dir =0
        self.frame=0
        self.velocity = 0
        self.event_que=[]
        self.cur_state = IdleState
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



