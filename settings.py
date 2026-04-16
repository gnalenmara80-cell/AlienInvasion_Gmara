from pathlib import Path

class Settings:
    """
    A class to store all settings for Alien Invasion.
    """
    def __init__(self):
        """Initialize the game's settings."""
        self.name = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 800
        self.Fps = 60

        # Background image path
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
