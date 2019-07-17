# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 18:51:31 2019

@author: imcna
"""
import pygame
from pygame.sprite import Sprite

class Invader(Sprite):
    """ Class to create the Aliens"""

    def __init__ (self, ai_settings, screen):
        """ Initialize Alien and start position """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the invader image and get its rect
        self.image = pygame.image.load('invader.png')
        #Need to resize the image
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        
        #Invader Position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Store decimal value for ships center
        self.x = float(self.rect.x)
        
        
    def blitme(self):
        """ Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
        
    def update(self):
        """ Move the invader right """
        self.x += (self.ai_settings.invader_speed *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x