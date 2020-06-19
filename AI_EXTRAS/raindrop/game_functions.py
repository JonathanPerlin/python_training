import sys

import pygame

from bullet import Bullet
from raindrop import Raindrop

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, bullets, screen, ship)

    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            return pygame.quit()
            pygame.quit()
            sys.exit()
            # exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
            
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def fire_bullet(ai_settings, bullets, screen, ship):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_raindrops_x(ai_settings, raindrop_width):
    """Determine the number of raindrops that fit in a row."""
    available_space_x = ai_settings.screen_width
    number_raindrops_x = int(available_space_x / (2 * raindrop_width))
    return number_raindrops_x


def get_number_rows(ai_settings, raindrop_height):
    """Determine the number of rows of raindrops that fit on the screen."""
    available_space_y = ai_settings.screen_height
    number_rows = int(available_space_y / raindrop_height)
    return number_rows

def create_raindrop(ai_settings, raindrops, screen, raindrop_number, row_number):
    """Create a raindrop and place it in the row."""
    raindrop = Raindrop(ai_settings, screen)
    raindrop.x = raindrop.rect.width + 2 * raindrop.rect.width * raindrop_number
    raindrop.rect.x = raindrop.x
    raindrop.y = 0 + 2 * raindrop.rect.height * row_number
    raindrop.rect.y = raindrop.y
    raindrops.add(raindrop)

def create_grid(ai_settings, screen, ship, raindrops):
    """Create a grid of raindrops."""
    # Create a raindrop and find the number of raindrops in a row.
    # Spacing between each raindrop is equal to one raindrop width.
    raindrop = Raindrop(ai_settings, screen)
    number_raindrops_x = get_number_raindrops_x(ai_settings, raindrop.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height)

    for row_number in range(number_rows):
        for raindrop_number in range(number_raindrops_x):
            create_raindrop(ai_settings, raindrops, screen, raindrop_number, row_number)

def check_grid_edges(ai_settings, raindrops, screen):
    """Respond appropriately if any raindrops have reached the bottom edge."""
    for raindrop in raindrops.sprites():
        if raindrop.check_edges():
            change_grid_direction(ai_settings, raindrops, screen)

def change_grid_direction(ai_settings, raindrops, screen):
    """Move the grid back to the top edge."""
    Raindrop(ai_settings, screen)
    for raindrop in raindrops.sprites():
        if raindrop.rect.y >= ai_settings.screen_height:
            raindrop.y = -raindrop.rect.height
            raindrop.rect.y = raindrop.y

def update_screen(ai_settings, screen, ship, raindrops, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets behind ship and raindrops.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    raindrops.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet position.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_raindrops(ai_settings, raindrops, screen):
    """Check if the grid is at the bottom edge and then update the positions of all raindrops in the grid."""
    check_grid_edges(ai_settings, raindrops, screen)
    raindrops.update()
