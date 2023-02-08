# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:01:50 2020

@author: Laura GALINDO
"""
class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        
        # High score should never be reset.
              # Load the high score.
        hs_file = 'highscore.txt'
        with open(hs_file, 'r') as f:
            try:
                self.high_score = int(float(f.read()))
            except:
                self.high_score = 0
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1