import game_framework
import pico2d

import start_state
import title_state
import stage1

pico2d.open_canvas()

game_framework.run(start_state)
game_framework.run(title_state)
game_framework.run(stage1)
pico2d.close_canvas()
# fill here
