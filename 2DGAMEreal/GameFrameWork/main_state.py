from pico2d import *
import game_world
import game_framework
import title_state
from MarioClass import Mario
from MapClass import *
from MonsterClass import *
name = "MainState"

mario=None

def enter():
    global mario
    global stage2
    global stage1
    global monster
    monster = Monster()
    stage1=Stage1()
    stage2= Stage2()
    mario=Mario()
    game_world.add_object(stage1,0)
    game_world.add_object(mario,1)
    game_world.add_object(monster, 1)


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





