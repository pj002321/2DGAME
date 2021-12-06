import game_world
from pico2d import *
import game_framework
import time
from Fire import FireBall
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP,LEFT_UP,JUMP_DOWN,JUMP_UP,FIRE_DOWN = range(7)


key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN,SDLK_SPACE): JUMP_DOWN,
    (SDL_KEYUP, SDLK_SPACE): JUMP_UP,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_1): FIRE_DOWN
}

PIXEL_PER_METER = (10.0 / 0.6) # 10 pixel 30 cm

# Run Speed
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Jump Speed
JUMP_SPEED_KMPH = 2.0
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH*1000.0/60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPM/60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS*PIXEL_PER_METER)

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
            mario.velocity += RUN_SPEED_PPS
        elif event == JUMP_DOWN :
            if mario.jumpchek == 1:
                if mario.jumpchek == 1:
                    mario.y += RUN_SPEED_PPS
                    if mario.y >= RUN_SPEED_PPS + 2:
                        mario.y -= RUN_SPEED_PPS
                        mario.jump = 2
                if mario.jumpchek == 2:
                    mario.y -= RUN_SPEED_PPS
                    if self.y <= 0:
                        self.y += RUN_SPEED_PPS
                        self.jump = 1




    def exit(mario,event):
        if event == FIRE_DOWN:
            mario.fire_ball()


    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time+1) % 2

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
        elif (event == JUMP_DOWN and mario.dir == 1) or (event == JUMP_DOWN and mario.dir == 0):
            mario.jump = 1


        mario.dir= clamp(-1, mario .velocity, 1)

    def exit(mario,event):
        if event == FIRE_DOWN:
            mario.fire_ball()

    def do(mario): # Do Activity
        mario.frame = (mario.frame+FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 5
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
        mario.frame=(mario.frame+FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time)%1
        mario.y += mario.velocity*game_framework.frame_time


    def draw(mario):
        if mario.dir == 1:
            mario.RJumpimage.clip_draw(int(mario.frame) * 40, 0, 40, 53, mario.x, mario.y)
        else:
            mario.LJumpimage.clip_draw(int(mario.frame) * 40, 0, 40, 53, mario.x, mario.y)



next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, JUMP_DOWN: JumpState,
                JUMP_UP: IdleState, FIRE_DOWN: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               JUMP_DOWN: JumpState, JUMP_UP: RunState, FIRE_DOWN: RunState},
    JumpState: {RIGHT_UP: RunState, LEFT_UP: RunState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, JUMP_UP: RunState,
                FIRE_DOWN: IdleState}
}

class Mario:

    def __init__(self):
        self.x, self.y = 50 // 2, 90
        self.LRunimage = load_image('MarioRunStateLeft.png')
        self.RRunimage = load_image('MarioRunStateRight.png')
        self.LJumpimage = load_image('MarioJumpStateLeft.png')
        self.RJumpimage = load_image('MarioJumpStateRight.png')
        self.Idleimage = load_image('MarioIdleState.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir =0
        self.key = 0
        self.frame=0
        self.velocity = 0
        self.event_que=[]
        self.cur_state = IdleState
        self.cur_state.enter(self,None)  # 현재 상태를 idlestate로 설정
        self.jump=1
        self.jumpchek=1

    def fire_ball(self):
        fire=FireBall(self.x,self.y,self.dir*3)
        fire.update()
        if self.dir==1:
            fire.dir=1
        if self.dir==0:
            fire.dir=0
        game_world.add_object(fire,1)

    def change_state(self,  state):
        # fill here
        pass


    def add_event(self, event):
        self.event_que.insert(0,event)

    def get_bb(self):
        return self.x-20,self.y-25,self.x+20,self.y+25

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que)>0:
            event = self.event_que.pop()
            self.cur_state.exit(self,event)
            self.cur_state=next_state_table[self.cur_state][event]
            self.cur_state.enter(self,event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type,event.key) in key_event_table:
            key_event = key_event_table[(event.type,event.key)]
            self.add_event(key_event)



