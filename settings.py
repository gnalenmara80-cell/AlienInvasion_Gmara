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
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_width = 40
        self.ship_height = 60
        self.ship_speed = 3
        # Bullet settings

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 5
        self.bullet_width = 25
        self.bullet_height = 80
        self.bullets_allowed = 5

