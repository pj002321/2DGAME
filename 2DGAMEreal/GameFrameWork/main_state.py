from pico2d import *
import random
import json
import os
from boy import Boy

import game_world
import game_framework
import title_state

name = "MainState"

boy=None

def enter():
    global boy
    boy=Boy()
    game_world.add_object(boy,0)


def exit():
    game_world.clear()  # 객체 지워짐


def pause():
    pass


def resume():
    pass


def handle_events():
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
    pass


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()  #
    update_canvas()
    pass





