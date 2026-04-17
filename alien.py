import pygame

from pygame.sprite import Sprite
from typing import TYPE_CHECKING


if TYPE_CHECKING:
   from alien_invasion import AlienInvasion

"""Module for the Alien class in the Alien Invasion game."""


class Alien(Sprite):
    """Represents an alien enemy in the Alien Invasion game."""

    def __init__(self, game: 'AlienInvasion', x: float, y: float):
        """Initialize the alien and set its starting position."""
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
        self.y = float(self.rect.y)

    def update(self):
        """Move the alien down the screen."""
        self.y += self.settings.bullet_speed
        self.rect.y = self.y

    def draw_alien(self):
        """Draw the alien on the screen."""
        self.screen.blit(self.image, self.rect)

