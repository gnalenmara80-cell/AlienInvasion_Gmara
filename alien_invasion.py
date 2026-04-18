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
from aresenal import Arsenal



class AlienInvasion:
    """Main game class for handling setup and the game loop."""

    def __init__(self):
        """Initialize pygame and create the game window."""
        pygame.init()
        self.settings = Settings()

        # Create the game window
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

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(str(self.settings.laser_sound))
        self.laser_sound.set_volume(0.7)


        self.ship = Ship(self, Arsenal(self))
        from alien_fleet import AlienFleet
        self.aliens = AlienFleet(self)


        
    def run_game(self):
        """Run the main game loop and handle events."""
     #game loop
        while self.running:
            self._check_events()
            self.ship.update()

            self.aliens.update_fleet()

            # Draw background image
            self._update_screen()

            # Limit FPS
            self.clock.tick(self.settings.Fps)


    def _update_screen(self):
        """Update the game screen by drawing the background and ship."""
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        self.ship.arsenal.draw()    
        for alien in self.aliens.fleet.sprites():
            alien.draw_alien()


        # Update the screen
        pygame.display.flip()

    def _check_events(self):
        """Check for and respond to user input events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
               self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
               self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        """Respond to key release events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
  

    def _check_keydown_events(self, event):
        """Respond to key press events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.ship.fire()
            # Play laser sound effect
            self.laser_sound.play()
            self.laser_sound.fadeout(250)  # Fade out the sound after 250 milliseconds


        elif event.key == pygame.K_q:
            # Quit the game
            self.running = False
            pygame.quit()
            sys.exit()



if __name__ == '__main__':
    # Create an instance of the game and run it
    ai = AlienInvasion()
    ai.run_game()
