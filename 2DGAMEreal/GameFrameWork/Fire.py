from pico2d import *
import game_world
PIXEL_PER_METER = (10.0 / 0.6) # 10 pixel 30 cm

# Run Speed
RUN_SPEED_KMPH = 10.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class FireBall:
    Fireimage=None
    def __init__(self,x=400,y=300,velocity=1):
        if FireBall.Fireimage==None:
            FireBall.Fireimage = load_image('Fire ball.png')
        self.x,self.y,self.velocity=x,y,velocity

        self.dir= Mario(self.dir)

    def draw(self):
        self.Fireimage.draw(self.x,self.y)

    def update(self):
        if self.dir==1:
            self.x += self.velocity+RUN_SPEED_PPS
        else:
            self.x -= self.velocity + RUN_SPEED_PPS
        if self.x<25 or self.x>1600-25:
            game_world.remove_object(self)