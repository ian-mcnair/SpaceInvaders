# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:45:31 2019

@author: imcna
"""

class GameStats():
    """ Tracks Statistics for the Game """
    def __init__(self, ai_settings):
        """ Initialize Statistics """
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        
    def reset_stats(self):
        """Stats that change during game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0