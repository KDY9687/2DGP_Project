from pico2d import *

class floor:
    def __init__(self):
        self.image = load_image('stage1_floor.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 80)