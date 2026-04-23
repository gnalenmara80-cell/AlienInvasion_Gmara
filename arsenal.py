import pygame
from bullet import Bullet
from typing import TYPE_CHECKING    

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion 
   
class Arsenal:
    """Handles the ship's arsenal, including bullets and firing mechanics."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the ship's arsenal with a reference to the game."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()  # Group to hold all active bullets   

    def update_arsenal(self):
        """Update the position of bullets and remove those that have disappeared."""
        self.arsenal.update()  
        self.remove_off_screen_bullets()
    
    def remove_off_screen_bullets(self):
        """Remove bullets that have moved off the top of the screen."""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draw all bullets in the arsenal on the screen."""
        for bullet in self.arsenal.sprites():
            bullet.draw()

    def fire_bullet(self):
        """Fire a bullet if the limit has not been reached."""
        if len(self.arsenal) < self.settings.bullets_allowed:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True  
        return False  
    
    def empty(self):
        self.arsenal.empty()
