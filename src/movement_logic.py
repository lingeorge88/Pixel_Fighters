from settings import VEL, HEIGHT, BORDER, WIDTH
import pygame
"""This file handles input from the keyboard and movement of the characters on the screen"""

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # Move Left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: #Move Right
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # Move up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: # Move down
        yellow.y += VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: # Move Left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #Move Right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: # Move up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: # Move down
        red.y += VEL