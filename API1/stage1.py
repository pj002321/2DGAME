import random
import json
import os

from pico2d import *
import game_framework
import title_state
name = "stage1"
World_WIDTH, World_HEIGHT = 1248, 440


class Monster:
    def __init__(self):
        self.mush=load_image('mushroom.png')
        self.turtle=load_image('turtleman.png')
        self.frame=0
        self.s_x=(World_WIDTH/2)
        self.s_y=80
        self.m_x=(World_WIDTH/2)
        self.m_y = 75
    def move(self):
        self.s_x -= 1
        self.m_x +=1
    def draw(self):
        self.frame=(self.frame+1)%2
        self.turtle.clip_draw(self.frame*16,0,16,29,self.s_x,self.s_y)
        self.mush.clip_draw(self.frame*16,0,16,20,self.m_x,self.m_y)


def move_events():
    global running
    global x,y
    global y2
    global dir
    global m_x
    global turn
    global jump
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                turn = 2
                dir+=3
                m_x-=10
            elif event.key == SDLK_LEFT:
                turn = 0
                dir-=3
                m_x +=10
            elif event.key == SDLK_SPACE:
                jump = y
                y2 = y+50
                for i in range(0,100+1,5):
                    t=i/100
                    y =(1-t)*jump+t*y2
                delay(0.0005)
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type ==SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                turn=2
                dir -= 3
            elif event.key == SDLK_LEFT:
                turn = 0
                dir += 3
                m_x += 20
            elif event.key == SDLK_SPACE:
                jump = y
                y2 = y - 50
                for i in range(0,100+1,1):
                    t=i/100
                    y =(1-t)*jump+t*y2
                delay(0.0005)


m_x = World_WIDTH
open_canvas(World_WIDTH, World_HEIGHT)
stage = load_image('World 1-1.png')
character1 = load_image('MM.png')
character2 = load_image('MM2.png')
monster=Monster()
running = True
x, y = World_WIDTH//2,90
y2=140
jump=0
dir = 0
frame1 = 0
frame2 = 0
turn = 0


while running:
    clear_canvas()
    stage.clip_draw(0, 100 * 1, 3447, 800, m_x, 100)
    monster.draw()
    monster.move()
    if turn ==0:
        character1.clip_draw(frame1 * 26, dir, 25, 55, x, y)
        frame1 = (frame1 + 1) % 5
    if turn==2:
        character2.clip_draw(frame2 * 26, dir, 25, 55, x, y)
        frame2 = (frame2+1) % 5

    update_canvas()

    move_events()
    delay(0.1)
    x += dir * 2

close_canvas()
