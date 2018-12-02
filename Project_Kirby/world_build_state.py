import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import main_state

from Kirby import kirby
from Floor import floor
from Background import background
from WaddleDee import waddledee


Kirby = None
Floor = None
Background = None

name = "WorldBuildState"

menu = None

def enter():
    global menu
    menu = load_image('start_window.png')
    hide_cursor()
    hide_lattice()

def exit():
    global menu
    pass

def pause():
    pass

def resume():
    pass

def get_kirby():
    return Kirby

def get_floor():
    return Floor

def get_background():
    return Background

def create_new_world():
    global Kirby
    global Floor
    global Background

    Floor = floor()
    game_world.add_object(Floor, 1)

    Kirby = kirby()
    game_world.add_object(Kirby, 1)

    Background = background()
    game_world.add_object(Background, 0)

    with open('waddledee_data.json', 'r') as f:
        waddledee_data_list = json.load(f)

    for data in waddledee_data_list:
        WaddleDee = waddledee(data['x'], data['y'])
        game_world.add_object(WaddleDee, 1)


def load_saved_world():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_n:
            create_new_world()
            game_framework.change_state(main_state)

def update():
    pass

def draw():
    clear_canvas()
    menu.draw(get_canvas_width()//2, get_canvas_height()//2)
    update_canvas()






