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
from settings import Settings

class AlienInvasion: 
    """
    Main game class for handling setup and the game loop.
    """
    def __init__(self):
        """
        Initialize pygame and create the game window.
        """

        pygame.init()
        self.settings = Settings() 

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file).convert()
        self.bg = pygame.transform.scale(self.bg,
                 (self.settings.screen_width, self.settings.screen_height)
                 )


        self.running = True
        self.clock = pygame.time.Clock()

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
                    

                    self.screen.blit(self.bg, (0, 0))
                    pygame.display.flip()
                    self.clock.tick(self.settings.Fps)  # Limit the frame rate to 60 FPS


if __name__ == '__main__':
   ai = AlienInvasion() 
   ai.run_game()