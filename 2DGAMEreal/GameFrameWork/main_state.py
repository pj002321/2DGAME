from pico2d import *
import game_world
import game_framework
import title_state
from MarioClass import Mario
from MapClass import Stage1
name = "MainState"

mario=None

def enter():
    global mario
    global stage
    stage=Stage1()
    mario=Mario()
    game_world.add_object(stage,0)
    game_world.add_object(mario,1)


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
        else:
            mario.handle_event(event)



    pass


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.1)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

    pass





