from pico2d import *
import game_world
PIXEL_PER_METER = (10.0 / 0.6) # 10 pixel 30 cm

# Run Speed
RUN_SPEED_KMPH = 5.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class FireBall:
    Fireimage=None
    global mario
    def __init__(self,x=0,y=80,velocity=1):
        if FireBall.Fireimage==None:
            FireBall.RFireimage = load_image('fireRight.png')
            FireBall.LFireimage = load_image('fireLeft.png')
        self.x,self.y,self.velocity=x,y,velocity
        self.dir=0
        self.font = load_font('ENCR10B.TTF', 16)

    def update(self):

        if self.dir==1:
            self.x += self.velocity+RUN_SPEED_PPS
        if self.dir==0:
            self.x -= self.velocity+RUN_SPEED_PPS
        if self.x<25 or self.x>3000:  # 삭제 조건
            game_world.remove_object(self)

    def get_bb(self):
        return self.x-10,self.y-5,self.x+10,self.y+5

    def draw(self):
        if self.dir == 1:
            self.RFireimage.draw(self.x,self.y)
        if self.dir == 0:
            self.LFireimage.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

