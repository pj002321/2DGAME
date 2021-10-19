import random

from pico2d import *
from random import randint
World_WIDTH, World_HEIGHT = 1048, 440

def handle_events():
    global running
    global x,y
    global dir
    global m_x
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir+=1

                m_x -=10
            elif event.key == SDLK_LEFT:
                dir-=1

                m_x +=10
            elif event.key == SDLK_SPACE:
                y+=30
            elif event.key == SDLK_ESCAPE:
                running == False
        elif event.type ==SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_SPACE:
                y-= 30

# def update_character():
#
#     global x, y
#     global ax, ay
#     global m_x
#     # x, y =ax, ay
#     t =  0.001
#
#     if SDL_KEYDOWN and SDLK_RIGHT:
#         x+=0.02
#         m_x -= 0.04
#
#     # if dist < 10 ** 2:
#     #     ax, ay = random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)


open_canvas(World_WIDTH, World_HEIGHT)
stage = load_image('World 1-1.png')
character = load_image('animation_sheet.png')
background = load_image('img.png')
running = True
x, y = World_WIDTH//2,100
m_x = World_WIDTH//2
dir=0
frame = 0

while running:
    clear_canvas()
    stage.clip_draw(0,100*1,3447,800,m_x,100)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y )
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir * 2



close_canvas()

