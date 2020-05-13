class Settings():
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230) # gray
        # self.bg_color = (111, 0, 255) # indigo

        # Ship settings
        self.ship_speed_factor = 15.5

        # Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
