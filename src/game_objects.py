"""
Define and manage game objects, including character positions.

This file contains the following functions:
- create_character_positions: Create initial positions for player characters.
"""

from settings import CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT
import pygame


def create_character_positions():
    """
    Create initial positions for player characters.

    Parameters:
    None

    Returns:
    tuple: Rectangles representing Player Two and Player One's positions.
    """
    # Create two pygame rect objects representing the rectangles of each character image on the game screen, at the specified positions
    player_two = pygame.Rect(700, 300, CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT)
    player_one = pygame.Rect(100, 300, CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT)
    return player_two, player_one
