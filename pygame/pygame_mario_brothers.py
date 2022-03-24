import imp


import collections
import dataclasses
import enum
import io
from turtle import position
import pygame
import urllib.request
import itertools as it
from random import randint

P = collections.namedtuple('P', 'x y')
D = enum.Enum('D', 'n e s w')
SIZE, MAX_SPEED = 50, P(5, 10)


def main():
    def get_screen():
        pygame.init()
        return pygame.display.set_mode(2 * [SIZE*16])

    def get_images():
        url = 'https://gto76.github.io/python-cheatsheet/web/mario_bros.png'
        img = pygame.image.load(io.BytesIO(urllib.request.urlopen(url).read()))

        return [img.subsurface(get_rect(x, 0)) for x in range(img.get_width() // 16)]

    def get_mario():
        Mario = dataclasses.make_dataclass(
            'Mario', 'rect spd facing_left frame_cycle'.split())

        return Mario(get_rect(1, 1), P(0, 0), False, it.cycle(range(3)))

    def get_titles():
        positions = [p for p in it.product(range(SIZE), repeat=2) if {*p} & {0, SIZE-1}] +\
            [(randint(1, SIZE-2), randint(2, SIZE-2))
             for _ in range(SIZE**2 // 10)]

        return [get_rect(*p) for p in positions]

    def get_rect(x, y):

        return pygame.Rect(x*16, y*16, 16, 16)

    run(get_screen(), get_images(), get_mario(), get_titles())
