from pico2d import *
import game_framework
import start_state
import main_state

pico2d.open_canvas(800,500)
game_framework.run(start_state)
game_framework.run(main_state)
pico2d.close_canvas()

