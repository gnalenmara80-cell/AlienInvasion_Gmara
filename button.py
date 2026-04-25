"""
Program Name: Alien Invasion - Button UI Component
Author: Gnalen Mara
Date: April 16, 2026

Purpose:
Defines a reusable Button class for menu interactions, including rendering,
text display, and click detection.

Starter Code Information:
UI button structure adapted from the Alien Invasion starter code provided
by RedBeard41 (Gabriel Walters) for CSCC coursework.
Original starter repository:
https://github.com/RedBeard441/alien_Invasion_starter
"""

import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Button:
    """A UI button that displays text, renders on screen, and detects mouse clicks."""

    def __init__(self, game: 'AlienInvasion', msg: str):
        """Initialize button properties, position, styling, and prepare its text image."""
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        # Correct pygame font usage
        self.font = pygame.font.Font(
            str(self.settings.font_file),
            self.settings.button_font_size
        )

        # Correct spelling: boundaries
        self.rect = pygame.Rect(0, 0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Render the button's text into an image and center it on the button."""
        self.msg_image = self.font.render(
            msg,
            True,
            self.settings.text_color,
            None
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draw the button and its text onto the game screen."""
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos):
        """Return True if the button was clicked based on the mouse position."""
        return self.rect.collidepoint(mouse_pos)
