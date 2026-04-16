"""
alien_invasion.py
Author: Gnalen Mara
Date: April 16, 2026
Purpose:
This module sets up the Alien Invasion game using pygame.
It initializes the game window, manages the main game loop,
and handles basic user events such as quitting the game.
"""

import sys
import pygame

class AlienInvasion: 
    """
    Main game class for handling setup and the game loop.
    """
    def __init__(self):
        """
        Initialize pygame and create the game window.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.running = True

    def run_game(self):
        """
        Run the main game loop and handle events.
        """
        #game loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                    
                    pygame.display.flip()

if __name__ == '__main__':
   ai = AlienInvasion() 
   ai.run_game()