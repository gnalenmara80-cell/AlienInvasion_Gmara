"""
Program Name: Alien Invasion - Alien Fleet Manager
Author: Gnalen Mara
Date: April 16, 2026

Purpose:
Manages the creation, layout, movement, and behavior of the alien fleet.
Handles fleet direction changes, edge detection, and coordinated movement.

Starter Code Information:
Based on fleet-management logic from the Alien Invasion starter code
provided by RedBeard41 (Gabriel Walters) for CSCC coursework.
Original starter repository:
https://github.com/RedBeard441/alien_Invasion_starter
"""

import pygame
from typing import TYPE_CHECKING
from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion    

"""Module for managing the fleet of alien objects in the Alien Invasion game."""


class AlienFleet:
    """Manages creation, positioning, movement, and collision behavior of the alien fleet."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize fleet manager, store references, and build the initial alien fleet."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.fleet = pygame.sprite.Group()
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        # Build the initial fleet
        self._create_fleet()
    
    def _create_fleet(self):
        """Create the full alien fleet and position it on the right side of the screen."""
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

        # UPDATED: Spawn fleet on the RIGHT side
        x_offset = screen_width - fleet_horizontal_space - 20

        # Keep your downward offset
        y_offset = 120

        for row in range(number_rows):
            for column in range(number_aliens_x):
                current_x = column * (alien_width + spacing) + x_offset
                current_y = row * (alien_height + spacing) + y_offset
                self._create_alien(current_x, current_y)
            

    def calculate_fleet_size(self, alien_width: int, screen_width: int, alien_height: int, screen_height: int):
        """Calculate how many aliens fit horizontally and how many rows fit vertically."""
        available_space_x = screen_width - (2 * alien_width)
        fleet_width = max(0, available_space_x // (alien_width + 10))

        fleet_height = screen_height - (3 * alien_height) - self.settings.ship_height
        number_rows = max(1, fleet_height // (2 * alien_height))
     
        number_rows = min(number_rows, 7)

        return fleet_width, number_rows


    def _create_alien(self, x: float, y: float):
        """Create a single alien at the specified (x, y) position and add it to the fleet."""
        alien = Alien(self.game, x, y)

        alien.x = float(alien.rect.x)
        alien.y = float(alien.rect.y)

        self.fleet.add(alien)
    


    def _check_fleet_edges(self):
        """Return True if any alien has reached the screen edge."""
        for alien in self.fleet.sprites():
            if alien.check_edges():
                return True
        return False 
            

    def update_fleet(self):
        """Update fleet movement and handle direction changes when edges are reached."""
        # UPDATED: Aliens move LEFT toward the ship
        if self._check_fleet_edges():
            self._change_fleet_direction()
        self.fleet.update() 

    def _change_fleet_direction(self):
        """Drop the fleet downward and reverse its horizontal direction."""
        for alien in self.fleet.sprites():
            alien.rect.y += self.fleet_drop_speed

        # UPDATED: Reverse horizontal direction (still works)
        self.settings.fleet_direction *= -1
        


    def draw_alien(self):
        """Draw all aliens in the fleet onto the screen."""
        for alien in self.fleet.sprites():
            alien.draw_alien()

    def check_collisions(self, other_group):
        """Check for collisions between aliens and another sprite group (e.g., bullets)."""
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_bottom(self):
        """Return True if any alien reaches the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.fleet.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                return True
        return False
    
    
    def check_destroyed_status(self):
        """Return True if all aliens in the fleet have been destroyed."""
        return len(self.fleet) == 0
