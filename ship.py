import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
   from alien_invasion import AlienInvasion

class Ship:
    

    def __init__(self, game: 'AlienInvasion' ):

        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.bounderies = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image,
           (self.settings.ship_width, self.settings.ship_height)

        )

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.bounderies.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

 
    def update(self):
         #update the position of the ship
         temp_speed = 3 * self.settings.ship_speed
         if self.moving_right and self.rect.right < self.bounderies.right:
            self.x += temp_speed 
         if self.moving_left and self.rect.left > self.bounderies.left:
            self.x -= temp_speed 


         self.rect.x = self.x
         

    def draw(self):
        self.screen.blit(self.image, self.rect)
