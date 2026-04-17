import pygame

from pygame.sprite import Sprite
from typing import TYPE_CHECKING


if TYPE_CHECKING:
   from alien_invasion import AlienInvasion

class Bullet(Sprite):

   def __init__(self, game: 'AlienInvasion'):
        """Initialize the bullet's position and settings."""
        super().__init__()
        self.game = game
        self.settings = game.settings
        self.screen = game.screen

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image,
           (self.settings.bullet_width, self.settings.bullet_height)
           )
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y) 


   def update(self):
        """Move the bullet up the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

   def draw(self):
        """Draw the bullet on the screen."""
        self.screen.blit(self.image, self.rect)

