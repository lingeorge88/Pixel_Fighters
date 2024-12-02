from settings import VEL, HEIGHT, BORDER, WIDTH
import pygame
"""This file handles input from the keyboard and movement of the characters on the screen"""

def player_one_handle_movement(keys_pressed, player_one):
    if keys_pressed[pygame.K_a] and player_one.x - VEL > 0:  # Move Left
        player_one.x -= VEL
    if keys_pressed[pygame.K_d] and player_one.x + VEL + player_one.width < BORDER.x:  # Move Right
        player_one.x += VEL
    if keys_pressed[pygame.K_w] and player_one.y - VEL > 0:  # Move up
        player_one.y -= VEL
    if keys_pressed[pygame.K_s] and player_one.y + VEL + player_one.height < HEIGHT - 15:  # Move down
        player_one.y += VEL

def player_two_handle_movement(keys_pressed, player_two):
    if keys_pressed[pygame.K_LEFT] and player_two.x - VEL > BORDER.x + BORDER.width:  # Move Left
        player_two.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and player_two.x + VEL + player_two.width < WIDTH:  # Move Right
        player_two.x += VEL
    if keys_pressed[pygame.K_UP] and player_two.y - VEL > 0:  # Move up
        player_two.y -= VEL
    if keys_pressed[pygame.K_DOWN] and player_two.y + VEL + player_two.height < HEIGHT - 15:  # Move down
        player_two.y += VEL
