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
from game_stats import GameStats    
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from time import sleep
from button import Button


class AlienInvasion:
    """Main game class for handling setup and the game loop."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()
        self.game_stats = GameStats(self.settings.starting_ship_count)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.name)

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

        # Game‑level arsenal + ship
        self.arsenal = Arsenal(self)
        self.ship = Ship(self)

        self.alien_fleet = AlienFleet(self)

        self.play_button = Button(self, 'play')
        self.game_active = False

    def run_game(self):
        """Run the main game loop and handle events."""
        try:
            while self.running:
                self._check_events()

                if self.game_active:
                    self.ship.update()
                    self.arsenal.update_arsenal()
                    self.alien_fleet.update_fleet()

                self._check_collisions()
                self._update_screen()
                self.clock.tick(self.settings.Fps)

        except Exception as e:
            print("GAME CRASHED WITH ERROR:", e)
            pygame.quit()
            sys.exit()
    

    def _check_collisions(self):
        """Check all collision types in the game."""

        # Ship hits alien
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()
            return

        # Alien hits bottom
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()
            return

        # Bullet hits alien
        collisions = self.alien_fleet.check_collisions(self.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)

        # All aliens destroyed
        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
    
    def _check_game_status(self):
        """Check the player's remaining ships and reset the level or end the game."""
        
        if self.game_stats.ship_limit > 0:
            self.game_stats.ship_limit -= 1
            self._reset_level()
            sleep(0.5)

        else:
            self.game_active = False


    def _reset_level(self):
        self.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet._create_fleet()
        pygame.display.flip()

    def restart_game(self):
        # setting up dynamic settings
        # reset Game stats
        # update HUD score
        # reset level
        # recenter the ship
        self.game_active = True
        pygame.mouse.set_visible(False)


    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))

        # Draw bullets
        self.arsenal.draw()

        # Draw ship
        self.ship.draw()

        # Draw aliens
        for alien in self.alien_fleet.fleet.sprites():
            alien.draw_alien()

        if not self.game_active:
            self.play_button.draw()    
            pygame.mouse.set_visible(True)

        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.new_method()

    def new_method(self):
        mouse_pos = pygame.mouse.get_pos() 
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()


    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_SPACE:
            if self.arsenal.fire_bullet():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)

        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
