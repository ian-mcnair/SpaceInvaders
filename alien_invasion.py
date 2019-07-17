# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:01:53 2019

@author: imcna
"""
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():
    """ Initialize game and create a screen object """
    pygame.init()
    
    # Create settings objects
    ai_settings = Settings()
    
    # Create window
    screen = pygame.display.set_mode((ai_settings.screen_width, 
                                      ai_settings.screen_height))
    # Change title of window
    pygame.display.set_caption('Alien Invasion')
    
    play_button = Button(ai_settings, screen, 'START')
    
    # Create statistics instance
    stats = GameStats(ai_settings)
    #Create ship object
    ship = Ship(ai_settings,screen)
    
    #Make group to store bullets
    bullets = Group()
    
    #Make group of Invaders
    invaders = Group()
    
    gf.create_fleet(ai_settings, screen, ship, invaders)
    
    #Running the Application
    while True:
        gf.check_events(ai_settings, screen, stats, play_button,
                        ship, invaders, bullets)
        
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, ship, invaders, bullets)
            gf.update_invaders(ai_settings, stats, screen, ship, invaders, bullets)
        
        gf.update_screen(ai_settings, screen, stats, ship, invaders, bullets, play_button)

# Calling function which runs entire app
run_game()

