import random
import json
import os

from pico2d import *
import game_framework
import game_world

from Kirby import kirby
from background import Background
from Floor import Floor


name = "MainState"

Kirby = None

def enter():
    global Kirby
    Kirby = kirby()
    background = Background()
    floor = Floor()
    #Floor = floor()
    game_world.add_object(background, 0)
    game_world.add_object(floor, 1)
    game_world.add_object(Kirby, 2)


def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            Kirby.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






