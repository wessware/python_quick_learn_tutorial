import sys

from numpy import alen
import pygame as pg
#from pygame.sprite import Sprite, Group
# initializing the game and setting a screen size


def run_game():

    pg.init()
    screen_dim = (1200, 800)
    screen = pg.display.set_mode(screen_dim)
    pg.display.set_caption('Git Catcher')

    # background color
    bg = (230, 230, 230)
    screen.fill(bg)

    # rectangle object
    rect_screen = screen.get_rect()

    # centering the rectangle
    screen_center = rect_screen.center

    """
    rect_screen.left, rect_screen.right
    rect_screen.top, rect_screen.bottom
    rect_screen.centerx, rect_screen.centery
    rect_screen.width, rect_screen.height

    rect_screen.size
    rect_screen.center
    """

    # creating a rect object
    amuni_rect = pg.Rect(100, 100, 3, 15)
    color = (100, 100, 100)
    pg.draw.rect(screen, color, amuni_rect)

    # pygame images
    ship_struc = pg.image.load('/images/reddit.png')

    ship_rect = ship_struc.get_rect()

    # image positioning
    ship_rect.midbottom = rect_screen.midbottom

    # drawing the ship on the screen
    screen.blit(ship_struc, ship_rect)

    # blitme() method is used when game objects are written in classes - to draw objects on the screen
    """
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    """
    # responding to keyboard inputs
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.type == pg.K_RIGHT:
                ship_rect.x += 1
            elif event.key == pg.K_LEFT:
                ship_rect.x -= 1
            elif event.key == pg.K_SPACE:
                ship_struc.fire_bullet()
            elif event.key == pg.K_q:
                sys.exit()

    # responding the key release
    if event.type == pg.KEYUP:
        if event.key == pg.K_RIGHT:
            ship_struc.moving_right = False
    # responding to mouse events
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            ship_struc.fire_bullet()

    """
        # finding the mouse position
        mouse_now = pg.mouse.get_pos()

        if button_rect.collidepoint(mouse_now):
            start_game()

        # hiding the mouse
        pg.mouse.set_visible(False)
   
    """

    # detecting object collision
    if pg.sprite.spritecollideany(ship_struc, aliens=0):
        ship_left -= 1

    # collision between two groups
    aliens = 0
    alien_point_value = 1
    collisions = pg.sprite.groupcollide(amuni_rect, aliens, True, True)

    score += len(collisions) * alien_point_value

    # rendering text
    msg = "You lost, play again?"
    msg_color = (100, 100, 100)
    bg_color = (230, 230, 230)

    f = pg.font.SysFont(None, 48)

    msg_image = f.render(msg, True, msg_color, bg_color)
    msg_image_rect = msg_image.get_rect()
    msg_image_rect.center = rect_screen.center
    screen.blit(msg_image, msg_image_rect)

  # start the main game loop
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        # screen refresh
        pg.display.flip()


run_game()
