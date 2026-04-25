"""
Program Name: Alien Invasion - Ship Class
Author: Gnalen Mara
Date: April 16, 2026

Purpose:
Defines the player's ship, including movement, rendering, image loading,
position resets, and collision behavior.

Starter Code Information:
Ship logic adapted from the Alien Invasion starter code provided by
RedBeard41 (Gabriel Walters) for CSCC coursework.
Original starter repository:
https://github.com/RedBeard441/alien_Invasion_starter
"""


import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
   from alien_invasion import AlienInvasion
  
class Ship:
    """Represents the player's ship in the game."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the ship with its starting position and settings."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.bounderies = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image, 
            (self.settings.ship_width, self.settings.ship_height)
        )

        self.rect = self.image.get_rect()
        self._center_ship()

        # UPDATED: vertical movement flags
        self.moving_up = False
        self.moving_down = False

    def _center_ship(self):
        # UPDATED: start ship on the LEFT edge, vertically centered
        self.rect.midleft = self.bounderies.midleft
        self.y = float(self.rect.y)

    def update(self):
        """Update the ship's position based on movement flags and boundaries."""
        self._update_ship_movement()

    def _update_ship_movement(self):
        temp_speed = self.settings.ship_speed

        # UPDATED: vertical movement only
        if self.moving_up and self.rect.top > self.bounderies.top:
            self.y -= temp_speed

        if self.moving_down and self.rect.bottom < self.bounderies.bottom:
            self.y += temp_speed

        self.rect.y = self.y

    def draw(self):
        """Draw the ship on the screen."""
        self.screen.blit(self.image, self.rect)

    def check_collisions(self, other_group):
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False
