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
    A class to store all settings for Alien Invasion.
    """
    def __init__(self):
        """Initialize the game's settings."""
        
        # Game window settings
        self.name = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 800
        self.Fps = 60


        # Background image path
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        # Ship settings
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship.png'
        self.ship_width = 50
        self.ship_height = 70
        self.ship_speed = 7
        self.starting_ship_count = 3




        # Bullet settings
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'beams.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'

        self.bullet_speed = 12
        self.bullet_width = 20
        self.bullet_height = 75
        self.bullets_allowed = 5


        # Alien settings
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_3.png'


        self.fleet_drop_speed = 15
        self.fleet_direction = 1  # 1 represents right; -1 represents left
        self.alien_width = 50
        self.alien_height = 50
        self.alien_speed = 3
        self.fleet_speed = 2
  






  