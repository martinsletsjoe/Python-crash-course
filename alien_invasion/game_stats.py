import json

class GameStats:
    '''Track statistics for Alien Invasion.'''

    def __init__(self, ai_game):
        '''Initialize statistics.'''
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.load_high_score()

    def load_high_score(self):
        """Load the high score from a file."""
        filename = 'high_score.json'
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                # If data is not an integer or None, set high score to 0
                self.high_score = int(data) if data is not None else 0
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            # If the file is not found or empty, set high score to 0
            self.high_score = 0

    def save_high_score(self):
        """Save the high score to a file."""
        filename = 'high_score.json'
        with open(filename, 'w') as file:
            json.dump(self.high_score, file)
    def reset_stats(self):
        '''Initialize statistics that can change during the game.'''
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1