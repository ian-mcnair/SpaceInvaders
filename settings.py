# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:18:45 2019

@author: imcna
"""

class Settings():
    """ A Class to store all settings for Alien Invasion """
    def __init__(self):
        """ Initialize the game's settings. """
        # General Settings
        self.screen_width = 1000
        self.screen_height = 900
        self.bg_color = (0,150,230)
        
        # Ship Settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        # Bullet Settings
        self.bullet_speed = 1
        self.bullet_width = 5050
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_limit = 5
        
        # Alien settings
        self.invader_speed = 0.5
        self.fleet_drop_speed = 10
        # 1 = right, -1 = left
        self.fleet_direction = 1 
        
        # How quickly the game speeds up
        self.speedup_scale = 10
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.invader_speed_factor = 1
        
        #Fleet direction
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Increase Speed Settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.invader_speed_factor *= self.speedup_scale