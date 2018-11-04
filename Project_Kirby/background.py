from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('Stage1_BG.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(800, 300)