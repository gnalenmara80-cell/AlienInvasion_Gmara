"""
alien_invasion.py
Author: Gnalen Mara
Date: April 16, 2026

Purpose:
Basic pygame setup and starter game loop.
"""

import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Main game class for handling setup and the game loop."""

    def __init__(self):
        """Initialize pygame and create the game window."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.name)

        # Load and scale background image
        self.bg = pygame.image.load(self.settings.bg_file).convert()
        self.bg = pygame.transform.scale(
            self.bg,
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.running = True
        self.clock = pygame.time.Clock()

        self.ship = Ship(self)

    def run_game(self):
        """Run the main game loop and handle events."""

        while self.running:
            self._check_events()

            # Draw background image
            self._update_screen()

            # Limit FPS
            self.clock.tick(self.settings.Fps)

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()


            # Update the screen
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
