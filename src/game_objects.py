from settings import CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT
import pygame

"""This file specifies the position of the characters on the screen"""
def create_character_positions():
    player_two = pygame.Rect(700, 300, CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT)
    player_one = pygame.Rect(100, 300, CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT)
    return player_two, player_one
