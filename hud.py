"""
Program Name: Alien Invasion - HUD (Heads-Up Display)
Author: Gnalen Mara
Date: April 16, 2026

Purpose:
Renders on-screen game information including score, high score, level, and
remaining lives. Handles font rendering and display updates.

Starter Code Information:
HUD concepts inspired by the Alien Invasion starter code provided by
RedBeard41 (Gabriel Walters) for CSCC coursework.
Original starter repository:
https://github.com/RedBeard441/alien_Invasion_starter
"""


import pygame.font


class HUD:
    """Handles all on‑screen score displays and life indicators for the game."""

    def __init__(self, game):
        """
        Initialize HUD with references to game objects and build initial images.

        Parameters:
            game (AlienInvasion): Main game instance providing settings, stats, and screen.
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.bounderies = game.screen.get_rect()
        self.game_stats = game.game_stats

        self.font = pygame.font.Font(
            self.settings.font_file,
            self.settings.HUD_font_size
        )

        self.padding = 20

        # Life image must be created BEFORE score/level positioning
        self._setup_life_image()

        # Build initial score + level images
        self.update_scores()
        self.update_level()
    
    def _setup_life_image(self):
        """
        Load and scale the ship image used to represent remaining lives.
        Creates:
            self.life_image
            self.life_rect
        """
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(
            self.life_image,
            (self.settings.ship_width, self.settings.ship_height)
        )
        self.life_rect = self.life_image.get_rect()
    
    def update_scores(self):
        """
        Update all score-related images:
        - High score (center top)
        - Max score (top right)
        - Current score (under max score)
        """
        self._update_hi_score()
        self._update_max_score()
        self._update_score()

    def update_level(self):
        """
        Update the level display text and position it under the life icons.
        """
        level_str = f"LEVEL: {self.game_stats.level:,}"
        self.level_image = self.font.render(
            level_str, True, self.settings.text_color, None
        )
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.life_rect.bottom + self.padding

    def _update_hi_score(self):
        """
        Render the high score and position it centered at the top of the screen.
        """
        hi_score_str = f"HI-SCORE: {self.game_stats.hi_score:,}"
        self.hi_score_image = self.font.render(
            hi_score_str, True, self.settings.text_color, None
        )
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.bounderies.centerx, self.padding)

    def _update_max_score(self):
        """
        Render the max score and position it at the top right of the screen.
        """
        max_score_str = f"MAX-SCORE: {self.game_stats.max_score:,}"
        self.max_score_image = self.font.render(
            max_score_str, True, self.settings.text_color, None
        )
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.bounderies.right - self.padding
        self.max_score_rect.top = self.padding

    def _update_score(self):
        """
        Render the current score and position it under the max score.
        """
        score_str = f"SCORE: {self.game_stats.score:,}"
        self.score_image = self.font.render(
            score_str, True, self.settings.text_color, None
        )
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.max_score_rect.right
        self.score_rect.top = self.max_score_rect.bottom + self.padding

    def _draw_lives(self):
        """
        Draw ship icons representing remaining lives.
        Lives appear at the top-left of the screen.
        """
        current_x = self.padding
        current_y = self.padding

        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding
  
    def draw(self):
        """
        Draw all HUD elements onto the screen:
        - High score
        - Max score
        - Current score
        - Level
        - Lives
        """
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()
