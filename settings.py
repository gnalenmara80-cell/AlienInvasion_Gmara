"""
settings.py
Author: Gnalen Mara
Date: April 16, 2026

Purpose:
Stores all the configuration settings for the Alien Invasion game.
"""

from pathlib import Path

class Settings:
    """
    Stores all static and dynamic configuration settings for the Alien Invasion game.

    This includes:
    - Window size and FPS
    - Asset file paths (images, sounds, fonts)
    - Ship, bullet, and alien properties
    - Button and HUD styling
    - Difficulty scaling
    """

    def __init__(self):
        """Initialize all static game settings."""
        
        # Game window settings
        self.name = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 800
        self.Fps = 60

        # Background image path
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        # Difficulty scaling factor for each level
        self.difficulty_scale = 1.1

        # High score file path
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        # Ship settings
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship.png'
        self.ship_width = 50
        self.ship_height = 70

        # Bullet settings
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'beams.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'
        
        # Alien settings
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_3.png'

        # Fleet movement direction (1 = right, -1 = left)
        self.fleet_direction = 1

        # Alien dimensions + speed
        self.alien_width = 50
        self.alien_height = 50
        self.alien_speed = 3
       
        # Button styling
        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 135, 50)

        # HUD styling
        self.text_color = (255, 255, 255)
        self.button_font_size = 45
        self.HUD_font_size = 18
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'

    def initialize_dynamic_settings(self):
        """
        Initialize settings that change throughout the game.

        These values reset when the player starts a new game.
        """
        self.ship_speed = 7
        self.starting_ship_count = 3
        self.bullet_speed = 12
        self.bullets_allowed = 5
        self.fleet_speed = 2
        self.fleet_drop_speed = 15
        self.bullet_width = 27
        self.bullet_height = 75
        self.alien_points = 50

    def increase_difficulty(self):
        """
        Increase game difficulty by scaling speed values.

        Called each time the player clears a full alien fleet.
        """
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
