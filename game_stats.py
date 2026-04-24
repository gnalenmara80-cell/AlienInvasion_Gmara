from pathlib import Path
import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class GameStats:

    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        """Load high score from JSON file if it exists."""
        self.path = self.settings.scores_file

        if self.path.exists() and self.path.stat().st_size > 0:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0

    def save_score(self):
        """Save high score to JSON file."""
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)

        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')

    def reset_stats(self):
        """Reset stats for a new game."""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

     
    def update(self, collisions):
        """Update score and max score after collisions."""
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()   

    def _update_score(self, collisions):
        """Increase score based on number of aliens hit."""
        for alien_list in collisions.values():
            for alien in alien_list:
                self.score += self.settings.alien_points

        print(f'Score: {self.score}, Max: {self.max_score}')

    def _update_max_score(self):
        """Update max score and high score."""
        if self.score > self.max_score:
            self.max_score = self.score
            self.hi_score = self.max_score
            self.save_score()  # auto-save high score
        print(f'Max: {self.max_score}')


    def _update_hi_score(self):
         """Update hi score and high score."""
         if self.score > self.hi_score:
             self.hi_score = self.score
             self.save_score()  # auto-save high score
         print(f'Hi Score: {self.hi_score}')

    def update_level(self):
        """Increase level when fleet is destroyed."""
        self.level += 1
        print(self.level)
