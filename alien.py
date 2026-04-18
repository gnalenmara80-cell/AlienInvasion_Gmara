import pygame

from pygame.sprite import Sprite
from typing import TYPE_CHECKING


if TYPE_CHECKING:
   from alien_invasion import AlienInvasion

"""Module for the Alien class in the Alien Invasion game."""


class Alien(Sprite):
    """Represents an alien enemy in the Alien Invasion game."""

    def __init__(self, game, x, y):
        super().__init__()
      
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
 
 
        
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image,
           (self.settings.alien_width, self.settings.alien_height)
           )
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the alien horizontally across the screen."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0
        
    def draw_alien(self):
        """Draw the alien on the screen."""
        self.screen.blit(self.image, self.rect)

