import sys

import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    
    ai_settings = Settings()
    
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship and a group of bullets.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    # Make an alien.
    alien = Alien(ai_settings, screen)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)

        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
    
run_game()
