# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:29:05 2019

@author: imcna
"""

import pygame

class Ship():
    def __init__ (self, ai_settings, screen):
        """ Initialize the ship and set its starting position """
        self.screen = screen
        self.ai_settings = ai_settings

        
        #Load the ship image and get its rect
        self.image = pygame.image.load('spaceship.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #Store decimal value for ships center
        self.center = float(self.rect.centerx)
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        
        
    def update(self):
        """Update the ships position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed
            
        # Update rect object from self.center   
        self.rect.centerx = self.center
        
    def blitme(self):
        """ Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        self.center = self.screen_rect.centerx