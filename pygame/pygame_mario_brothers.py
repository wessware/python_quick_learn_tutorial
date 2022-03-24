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


def run(screen, images, mario, titles):
    clock = pygame.time.Clock()

    while all(event.type != pygame.QUIT for event in pygame.event.get()):
        keys = {pygame.K_UP: D.n, pygame.K_RIGHT: D.e,
                pygame.K_DOWN: D.s, pygame.K_LEFT: D.w}
        pressed = {keys.get(i) for i, on in enumerate(
            pygame.key.get_pressed()) if on}
        update_speed(mario, tiles, pressed)
        update_position(mario, tiles)
        draw(screen, images, mario, tiles, pressed)
        clock.tick(28)


def update_speed(mario, tiles, pressed):
    x, y = mario.spd
    x += 2 * ((D.e in pressed) - (D.w in pressed))
    x -= x // abs(x) if x else 0
    y += 1 if D.s not in get_boundaries(mario.rect,
                                        tiles) else (-10 if D.n in pressed else 0)
    mario.spd = P(*[max(-limit, min(limit, s))
                  for limit, s in zip(MAX_SPEED, P(x, y))])


def update_position(mario, tiles):
    new_p = mario.rect.topleft
    larger_speed = max(abs(s) for s in mario.spd)

    for _ in range(larger_speed):
        mario.spd = stop_on_collision(
            mario.spd, get_boundaries(mario.rect, tiles))
        new_p = P(*[a + s/larger_speed for a, s in zip(new_p, mario_spd)])
        mario.rect.topleft = new_p


def get_boundaries(rect, tiles):
    deltas = {D.n: P(0, -1), D.e: P(1, 0), D.s: P(0, 1), D.w: P(-1, 0)}

    return {d for d, delta in deltas.items() if rect.move(delta).collidelist(tiles) != -1}


def stop_on_collision(spd, bounds):

    return P(x=0 if (D.w in bounds and spd.x < 0) or (D.e in bounds and spd.x > 0) else spd.x,
             y=0 if (D.n in bounds and spd.y < 0) or (D.s in bounds and spd.y > 0) else spd.y)
