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

        self.impact_sound = pygame.mixer.Sound(str(self.settings.impact_sound))
        self.impact_sound.set_volume(0.7)



        self.ship = Ship(self, Arsenal(self))
        from alien_fleet import AlienFleet
        self.alien_fleet = AlienFleet(self) 
        
    def run_game(self):
        """Run the main game loop and handle events."""
     #game loop
        while self.running:
            self._check_events()
            self.ship.update()

            self.alien_fleet.update_fleet()  # Update the position of the alien fleet
            self._check_collisions()

            # Draw background image
            self._update_screen()

            # Limit FPS
            self.clock.tick(self.settings.Fps)


    def _check_collisions(self):
         # check collision for ship
         if self.ship.check_collisions(self.alien_fleet.fleet): 
             self._reset_level()  # Reset the level if the ship collides with an alien

             
         #subtract one life if possible


        # check collision for aliens and bottom of screen
         if self.alien_fleet.check_fleet_bottom():
            self._reset_level()  # Reset the level if any alien reaches the bottom of the

        # check collision for projectiles and aliens    
         collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal) 
         
         if collisions:
             self.impact_sound.play()
             self.impact_sound.fadeout(500)


        





           # check collisions of projectiles and aliens
         


    def _reset_level(self):
        self.ship.ship.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet._create_fleet()



    def _update_screen(self):
        """Update the game screen by drawing the background and ship."""
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        self.ship.arsenal.draw()    
        for alien in self.alien_fleet.fleet.sprites():
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
