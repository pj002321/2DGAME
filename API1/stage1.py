import random
import json
import os

from pico2d import *
import game_framework
name = "stage1"
World_WIDTH, World_HEIGHT = 1048, 440

def handle_event():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()


def handle_events():
    global running
    global cx,cy
    global y1,y2
    global dir
    global m_x
    global turn
    global t
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                turn = 0
                dir+=3
            elif event.key == SDLK_LEFT:
                turn = 60
                dir-=3
            elif event.key == SDLK_SPACE:
                for i in range(0, 100, 1):
                    t=i/100
                    cy=(1-t)*y1+t*y2
                delay(0.0005)
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type ==SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                turn=0
                dir -= 3
            elif event.key == SDLK_LEFT:
                turn = 60
                dir += 3
            elif event.key == SDLK_SPACE:
                for i in range(0,100,1):
                    t=i/1000
                    cy=(1-t)*y1+t*y2
                delay(0.0005)
m_x = World_WIDTH
open_canvas(World_WIDTH, World_HEIGHT)
stage = load_image('World 1-1.png')
character = load_image('marioss.png')
running = True
cx, cy = World_WIDTH//2,90
y1,y2 = 80,150
jump=0
dir = 0
frame = 0
turn = 0
t=0.1
while running:
    clear_canvas()
    stage.clip_draw(0, 100 * 1, 3447, 800, m_x, 100)
    character.clip_draw(frame * 35,turn, 35, 60, cx, cy)
    frame = (frame + 1) % 5
    update_canvas()

    handle_events()
    delay(0.1)
    cx += dir * 1
    m_x -= dir * 4
    if cx>=250 and cx<=350:
        m_x += dir*5
    elif cx<=1050 and cx>=950:
        m_x += dir*5


close_canvas()
