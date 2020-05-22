import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
    # Initialize pygame, settings, and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Make a ship, a group of bullets, and a group of raindrops.
    ship = Ship(screen, ai_settings)
    bullets = Group()
    raindrops = Group()

    # Create the grid of raindrops.
    gf.create_grid(ai_settings, screen, ship, raindrops)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_raindrops(ai_settings, raindrops, screen)
        gf.update_screen(ai_settings, screen, ship, raindrops, bullets)

run_game()
