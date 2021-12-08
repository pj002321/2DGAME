from pico2d import *
import game_framework
import start_state
import main_state

pico2d.open_canvas(1000,400)
game_framework.run(main_state)
pico2d.close_canvas()

