"""
Contains functions that handle player movement based on keyboard inputs

This file contains the following functions:
- player_one_handle_movement: Handle Player One's movement.
- player_two_handle_movement: Handle Player Two's movement.
"""

from settings import VEL, HEIGHT, BORDER, WIDTH
import pygame


def player_one_handle_movement(keys_pressed, player_one):
    """
    Handle Player One's movement based on keyboard input.

    Parameters:
    keys_pressed (pygame.key.ScancodeWrapper): Pygame's built-in method that tracks that state of all keys.
    player_one (pygame.Rect): Player One's rectangle object.

    Returns:
    None
    """
    # we also need to check that the character is moving within the dimensions of the game screen before moving the character
    if keys_pressed[pygame.K_a] and player_one.x - VEL > 0:  # Move Left
        player_one.x -= VEL
    if (
        keys_pressed[pygame.K_d] and player_one.x + VEL + player_one.width < BORDER.x
    ):  # Move Right
        player_one.x += VEL
    if keys_pressed[pygame.K_w] and player_one.y - VEL > 0:  # Move up
        player_one.y -= VEL
    if (
        keys_pressed[pygame.K_s]
        and player_one.y + VEL + player_one.height < HEIGHT - 15
    ):  # Move down
        player_one.y += VEL


def player_two_handle_movement(keys_pressed, player_two):
    """
    Handle Player Two's movement based on keyboard input.

    Parameters:
    keys_pressed (pygame.key.ScancodeWrapper): Pygame's built-in method that tracks that state of all keys.
    player_two (pygame.Rect): Player two's rectangle object.

    Returns:
    None
    """
    # we also need to check that the character is moving within the dimensions of the game screen before moving the character
    if (
        keys_pressed[pygame.K_LEFT] and player_two.x - VEL > BORDER.x + BORDER.width
    ):  # Move Left
        player_two.x -= VEL
    if (
        keys_pressed[pygame.K_RIGHT] and player_two.x + VEL + player_two.width < WIDTH
    ):  # Move Right
        player_two.x += VEL
    if keys_pressed[pygame.K_UP] and player_two.y - VEL > 0:  # Move up
        player_two.y -= VEL
    if (
        keys_pressed[pygame.K_DOWN]
        and player_two.y + VEL + player_two.height < HEIGHT - 15
    ):  # Move down
        player_two.y += VEL
