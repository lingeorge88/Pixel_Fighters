from settings import CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT
import pygame

"""This file specifies the position of the characters on the screen"""
def create_character_positions():
    red = pygame.Rect(700, 300, CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT)
    yellow = pygame.Rect(100, 300, CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT)
    return red, yellow