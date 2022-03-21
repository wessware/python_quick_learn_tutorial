# Python Curses


# clears the terminal, prints a message and wait to the ESC key action
from curses import wrapper, curs_set, ascii
from curses import KEY_UP, KEY_RIGHT, KEY_DOWN, KEY_LEFT

from matplotlib.pyplot import draw


def main():
    wrapper(draw)


def draw(screen):
    curs_set(0)
    screen.nodelay(True)
    screen.clear()
    screen.addstr(0, 0, 'Cursed! Press ESC to Exit')

    while screen.getch() != ascii.ESC:
        pass


def get_border(screen):
    from collections import namedtuple
    P = namedtuple('P', 'x y')
    height, width = screen.getmaxyx()

    return P(width-1, height-1)


if __name__ == '__main__':
    main()
