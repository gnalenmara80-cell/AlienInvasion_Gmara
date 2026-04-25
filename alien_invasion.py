"""
Program Name: Alien Invasion
Author: Gnalen Mara
Date: April 16, 2026

Purpose:
Main entry point for the Alien Invasion game. This file initializes the game,
manages the main loop, handles user input, updates game objects, and renders
all visual elements to the screen.

Starter Code Information:
This project is based on the Alien Invasion starter code provided by
RedBeard41 (Gabriel Walters) for CSCC Software Development coursework.
Original starter repository:
https://github.com/RedBeard441/alien_Invasion_starter
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
from hud import HUD


class AlienInvasion:
    """Main game controller class."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file).convert()
        self.bg = pygame.transform.scale(
            self.bg,
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.game_stats = GameStats(self)
        self.HUD = HUD(self)

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(str(self.settings.laser_sound))
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(str(self.settings.impact_sound))
        self.impact_sound.set_volume(0.7)

        self.arsenal = Arsenal(self)
        self.ship = Ship(self)
        self.alien_fleet = AlienFleet(self)

        self.play_button = Button(self, 'play')
        self.game_active = False

    def run_game(self):
        """Main game loop that processes events, updates objects, and redraws the screen."""
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
        """Handle ship collisions, bullet hits, and level progression."""
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()
            return

        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()
            return

        collisions = self.alien_fleet.check_collisions(self.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
            self.game_stats.update(collisions)
            self.HUD.update_scores()

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            self.game_stats.update_level()
            self.HUD.update_level()

    
    def _check_game_status(self):
        """Handle ship loss and game over conditions."""
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False


    def _reset_level(self):
        """Reset bullets, rebuild alien fleet, and refresh screen."""
        self.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet._create_fleet()
        pygame.display.flip()

    def restart_game(self):
        """Start a new game session and reset all dynamic systems."""
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)


    def _update_screen(self):
        """Draw all game elements and update the display."""
        self.screen.blit(self.bg, (0, 0))
        self.arsenal.draw()
        self.ship.draw()
        self.HUD.draw()

        for alien in self.alien_fleet.fleet.sprites():
            alien.draw_alien()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()

    def _check_events(self):
        """Process keyboard, mouse, and quit events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_stats.save_scores()
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN and self.game_active:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.new_method()

    def new_method(self):
        """Handle play button click."""
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()


    def _check_keyup_events(self, event):
        """Stop ship movement when arrow keys are released."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_keydown_events(self, event):
        """Handle key presses for movement, firing, and quitting."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        elif event.key == pygame.K_SPACE:
            if self.arsenal.fire_bullet():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)

        elif event.key == pygame.K_q:
            self.running = False
            self.game_stats.save_scores()
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
