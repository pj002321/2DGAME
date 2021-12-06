from pico2d import *
import game_world
import game_framework
import title_state
from MarioClass import*
from MapClass import Stage1
from MonsterClass import *
from Fire import FireBall
name = "MainState"


mario=None
stage1=None
monsters=[]
tutles=None
fire=None


def collide(a,b):
    left_a,bottom_a,right_a,top_a = a.get_bb()
    left_b,bottom_b,right_b,top_b = b.get_bb()

    if left_a>right_b:return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True




def enter():
    global stage1
    stage1=Stage1()
    game_world.add_object(stage1,0)

    global mario
    mario=Mario()
    game_world.add_object(mario,1)

    global fire
    fire = FireBall()
    game_world.add_object(fire, 1)

    global monsters
    monsters = [Mush() for i in range(4)]
    game_world.add_objects(monsters, 1)

    global turtles
    turtles = [Turtle() for i in range(3)]
    game_world.add_objects(turtles, 1)



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

def update():
    global monsters
    global fire
    for game_object in game_world.all_objects():
        game_object.update()

    for monster in monsters:
        if collide(mario,monster):
            monsters.remove(monster)
            game_world.remove_object(monster)

        if collide(fire, monster):
            monsters.remove(monster)
            game_world.remove_object(monster)

    for turtle in turtles:
        if collide(mario,turtle):
            turtles.remove(turtle)
            game_world.remove_object(turtle)

        if collide(turtle, fire):
            monsters.remove(turtle)
            game_world.remove_object(turtle)

    delay(0.03)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







