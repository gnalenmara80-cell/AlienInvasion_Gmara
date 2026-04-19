"""
ship.py
Author: Gnalen Mara
Date: April 16, 2026

Purpose:
Handles the player's ship in the Alien Invasion game, including movement and drawing.
"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
   from alien_invasion import AlienInvasion
   from aresenal import Arsenal
  
class Ship:
    """Represents the player's ship in the game."""

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal' = None):
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
        self.moving_right = False
        self.moving_left = False
       
        self.arsenal = arsenal

    def _center_ship(self):
        self.rect.midbottom = self.bounderies.midbottom
        self.x = float(self.rect.x)

 
    def update(self):
        """Update the ship's position based on movement flags and boundaries."""
        # update the position of the ship
        self._update_ship_movement()
        self.arsenal.update_arsenal()  # Update the position of bullets in the arsenal

    def _update_ship_movement(self):
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.bounderies.right:
               self.x += temp_speed

        if self.moving_left and self.rect.left > self.bounderies.left:
               self.x -= temp_speed

        self.rect.x = self.x

    def draw(self):
        """Draw the ship on the screen."""
        self.screen.blit(self.image, self.rect)

    def fire(self):
        return self.arsenal.fire_bullet()  # Attempt to fire a bullet and return the result
    

    
    def check_collisions(self, other_group):
         if pygame.sprite.spritecollideany(self, other_group):
           self._center_ship()
           return True
         return False 