import game_framework
from pico2d import *
import start_state
import main_state

pico2d.open_canvas()
game_framework.run(start_state)
game_framework.run(main_state)
pico2d.close_canvas()

