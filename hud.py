"""
HUD module for Alien Invasion.
Displays the player's score, max score, and high score on screen.
Author: Gnalen Mara
Date: April 2026
"""

import pygame.font


class HUD:
    """Handles all on‑screen score displays for the game."""

    def __init__(self, game):
        """Initialize HUD with game references and build initial score images."""
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
        self.update_scores()

    def update_scores(self):
        """Update all score images (hi‑score, max‑score, score)."""
        self._update_hi_score()
        self._update_max_score()
        self._update_score()

    def _update_hi_score(self):
        """Render the high score and position it centered at the top."""
        hi_score_str = f"HI-SCORE: {self.game_stats.hi_score:,}"
        self.hi_score_image = self.font.render(
            hi_score_str, True, self.settings.text_color, None
        )
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.bounderies.centerx, self.padding)

    def _update_max_score(self):
        """Render the max score and position it at the top right."""
        max_score_str = f"MAX-SCORE: {self.game_stats.max_score:,}"
        self.max_score_image = self.font.render(
            max_score_str, True, self.settings.text_color, None
        )
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.bounderies.right - self.padding
        self.max_score_rect.top = self.padding

    def _update_score(self):
        """Render the current score and position it under the max score."""
        score_str = f"SCORE: {self.game_stats.score:,}"
        self.score_image = self.font.render(
            score_str, True, self.settings.text_color, None
        )
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.bounderies.right - self.padding
        self.score_rect.top = self.max_score_rect.bottom + self.padding

    def draw(self):
        """Draw all HUD elements onto the screen."""
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
