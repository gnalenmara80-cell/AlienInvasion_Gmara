import pygame
from typing import TYPE_CHECKING
from alien import Alien


if TYPE_CHECKING:
    from alien_invasion import AlienInvasion    
""" Module for managing the fleet of aliens objects. """



class AlienFleet:
    """Manages a fleet of aliens in the Alien Invasion game."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the fleet and set its starting position."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.fleet = pygame.sprite.Group()
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self._create_fleet()
    
    def _create_fleet(self):
        """Create a full fleet of aliens."""
        alien_width = self.settings.alien_width
        alien_height = self.settings.alien_height
        screen_width = self.settings.screen_width
        screen_height = self.settings.screen_height

        spacing = 10
        number_aliens_x, number_rows = self.calculate_fleet_size(
        alien_width, screen_width, alien_height, screen_height
    )
        

        fleet_horizontal_space = number_aliens_x * (alien_width + spacing)
        fleet_vertical_space = number_rows * (alien_height + spacing)   
        x_offset = int((screen_width - fleet_horizontal_space) // 2)
        y_offset = 0


        for row in range(number_rows):
            for column in range(number_aliens_x):
                current_x = column * (alien_width + spacing) + x_offset
                current_y = row * (alien_height + spacing) + y_offset
                self._create_alien(current_x, current_y)
            

    def calculate_fleet_size(self, alien_width: int, screen_width: int, alien_height: int, screen_height: int):
    
     available_space_x = screen_width - (2 * alien_width)
     fleet_width = available_space_x // (alien_width + 10)

     fleet_height = screen_height - (3 * alien_height) - self.settings.ship_height
     number_rows = fleet_height // (2 * alien_height)

     # limit rows so fleet stays at the top
     number_rows = min(number_rows, 6)

     return fleet_width, number_rows


    def _create_alien(self, x: float, y: float):
        """Create an alien and place it in the fleet."""
        alien = Alien(self.game, x, y)

        alien.x = float(alien.rect.x)
        alien.y = float(alien.rect.y)   
        self.fleet.add(alien)
    



    def _check_fleet_edges(self):
        
        """Check if any aliens have reached an edge, and return True if so."""
        for alien in self.fleet.sprites():
            if alien.check_edges():
                return True
        return False 
            

    def update_fleet(self):
        
        """Update the positions of all aliens in the fleet."""
        if self._check_fleet_edges():
            self._change_fleet_direction()
        self.fleet.update() 

    def _change_fleet_direction(self):
        """ Drop the entire fleet and change its direction"""
        for alien in self.fleet.sprites():
            alien.rect.y += self.fleet_drop_speed
        self.settings.fleet_direction *= -1
        


    def draw_alien(self):
        """Draw the alien on the screen."""
        for alien in self.fleet.sprites():
            alien.draw_alien()
