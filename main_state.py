from pico2d import *
import Fire
import MapClass
import MonsterClass
import MonsterClass2
import game_world
import game_framework
import title_state
from MarioClass import Mario
from background import InfiniteBackground as Background
from MonsterClass import *
from MonsterClass2 import *
from Fire import FireBall
from NomalBlock import Nomalblock
from ItemBlock import ItemBlock
from ITEM_STAR import ItemStar
name = "MainState"
import Server
import collide


def enter():

    Server.monsters = MonsterClass.Mush()
    Server.tutles=MonsterClass2.Turtle()
    Server.mario=Mario()
    Server.fire=Fire.FireBall()
    Server.ground=Background()
    Server.itemBlock = ItemBlock()
    Server.item_star=ItemStar()
    Server.nomalblock = Nomalblock()


    Server.stage1=Stage1()
    game_world.add_object(Server.ground,0)


    Server.mario=Mario()
    game_world.add_object(Server.mario,1)


    Server.fire = FireBall()
    game_world.add_object(Server.fire, 1)


    Server.monsters = [Mush() for i in range(4)]
    game_world.add_objects(Server.monsters, 1)


    Server.tutles = [Turtle() for i in range(3)]
    game_world.add_objects(Server.tutles, 1)

    Server.nomalblock = [Nomalblock() for i in range(20)]
    game_world.add_objects(Server.nomalblock,1)

    Server.itemblock = [ItemBlock() for i in range(15)]
    game_world.add_objects(Server.itemblock, 1)

    Server.item_star = [ItemStar() for _ in range(15)]
    game_world.add_objects(Server.item_star, 1)




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
            Server.mario.handle_event(event)

def update():

    for game_object in game_world.all_objects():
        game_object.update()



    delay(0.03)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







