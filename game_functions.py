# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:49:56 2019

@author: imcna
"""
import pygame
import sys
from bullet import Bullet
from invader import Invader 
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to key press events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    if event.key == pygame.K_q:
        pygame.quit()
        sys.exit()
        
def fire_bullet(ai_settings, screen, ship, bullets):
    """ Fire a bullet"""
    if len(bullets) < ai_settings.bullet_limit:
        new_bullet = Bullet(ai_settings, screen,ship)
        bullets.add(new_bullet)
        
def check_keyup_events(event, ship):
    """ Respond to key release events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, play_button, ship, invaders, 
                 bullets):
    """Responds to keypresses and mouse events"""
    for event in pygame.event.get():
        # Handles Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, 
                              invaders, bullets, mouse_x, mouse_y)
            
        # Handles all Key Presses
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # Handles all Key Releases
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def check_play_button(ai_settings, screen, stats, play_button, ship, invaders, 
                      bullets, mouse_x, mouse_y):
    """Starts a new game when the player clicks Play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Rest game Settings
        ai_settings.initialize_dynamic_settings()
        
        # Hiding mouse after play button pressed
        pygame.mouse.set_visible(False)
        
        # Resetting screen
        stats.reset_stats()
        stats.game_active = True
        invaders.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, invaders)
        ship.center_ship()
        

def update_screen(ai_settings, screen, stats, ship, invaders, bullets, play_button):
    """Updates images on the creen and flip to the new screen"""
    # Redraw Screen during each loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    invaders.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullets()
    if not stats.game_active:
        play_button.draw_button()
    # Make most recent screen avaliable
    pygame.display.flip()
    
def update_bullets(ai_settings, screen, ship, invaders, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_invader_collisions(ai_settings, screen, ship, invaders, bullets)
        
def check_bullet_invader_collisions(ai_settings, screen, ship, invaders, bullets):   
    pygame.sprite.groupcollide(bullets, invaders, True, True)
    if len(invaders) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, invaders)
            
def create_fleet(ai_settings, screen, ship, invaders):
    """ Create a set of invaders """
    invader = Invader(ai_settings, screen)
    num_invader_x = get_num_invaders_x(ai_settings, invader.rect.width) 
    num_rows = get_num_rows(ai_settings, ship.rect.height, invader.rect.height)
    # Creating the first rorw of invaders
    for row_num in range(num_rows):
        for invader_num in range (num_invader_x):
            create_invader(ai_settings, screen, invaders, invader_num, row_num)

def get_num_invaders_x(ai_settings, invader_width):
    space_left_x = ai_settings.screen_width - 2 * invader_width
    num_invader_x = int(space_left_x / (2 * invader_width))
    return num_invader_x

def create_invader(ai_settings, screen, invaders, invader_num, row_num):
    invader = Invader(ai_settings, screen)
    invader_width = invader.rect.width
    invader.x = invader_width + 2 * invader_width * invader_num
    invader.rect.x = invader.x
    invader.rect.y = invader.rect.height + 2 * invader.rect.height * row_num
    invaders.add(invader)
    
def get_num_rows(ai_settings, ship_height, invader_height):
    """Determine number of rows that will fit on the screen"""
    space_left_y = (ai_settings.screen_height -
                    (3 * invader_height) - ship_height)
    return int(space_left_y / (2*invader_height))

def check_fleet_edges(ai_settings, invaders):
    for invader in invaders.sprites():
        if invader.check_edges():
            change_fleet_direction(ai_settings, invaders)
            break
        
def change_fleet_direction(ai_settings, invaders):
    for invader in invaders.sprites():
        invader.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_invaders(ai_settings, stats, screen, ship, invaders, bullets):
    """Update the positions of all the invaders in the fleet"""
    check_fleet_edges(ai_settings, invaders)
    invaders.update()
    if pygame.sprite.spritecollideany(ship,invaders):
        ship_hit(ai_settings, stats, screen, ship, invaders, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, invaders, bullets)
            
def ship_hit(ai_settings, stats, screen, ship, invaders, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        invaders.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, invaders)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, invaders, bullets):
    screen_rect = screen.get_rect()
    for invader in invaders.sprites():
        if invader.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, invaders, bullets)
            break