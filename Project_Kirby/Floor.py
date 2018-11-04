from pico2d import *

class Floor:
    def __init__(self):
        self.image = load_image('Stage1_Floor.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 80)