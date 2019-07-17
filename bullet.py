# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:59:55 2019

@author: imcna
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A Class to manage bullets fired from ship """
    
    def __init__(self, ai_settings, screen, ship):
        """Creates a bullet object at the ships' current position"""
        super().__init__()
        self.screen = screen
        
        #Create the bullet rect
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #Store position as decimal
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed
    
    def update(self):
        """Move the bullet the screen"""
        # Update the decimal position of the bullet
        self.y -= self.speed_factor
        
        # Update the rect position
        self.rect.y = self.y
        
    def draw_bullets(self):
        """ Draw the bullet to the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)
        