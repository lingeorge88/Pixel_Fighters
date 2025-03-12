"""
The file handles shooting logic and projectile interactions.

This file contains the following functions:
- handle_player_one_shooting: Handle shooting logic for Player One.
- handle_player_two_shooting: Handle shooting logic for Player Two.
- handle_projectiles: Move projectiles, check collisions, and clean up off-screen projectiles.
"""

import pygame
from settings import (
    PROJCT_VEL,
    MAX_PROJCT,
    WIDTH,
    PLAYER_ONE_HIT,
    PLAYER_TWO_HIT,
    PLAYER_ONE_PROJECTILE,
    PLAYER_TWO_PROJECTILE,
)
from game_sound import SoundManager
from projectile import Projectile

# initialize an instance of the sound manager class so we can play the sound effects when each player fires and gets hit
gameSound = SoundManager()


def handle_player_one_shooting(event, player_one, player_one_projectiles):
    """
    Handle shooting logic for Player One.

    Parameters:
    event (pygame.Event): The event triggering shooting.
    player_one (pygame.Rect): Player One's rectangle object.
    player_one_projectiles (list): List of Player One's projectiles.

    Returns:
    None
    """
    # Check if the event is a key press and if the 'Q' key was pressed
    if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
        # Ensure the number of projectiles does not exceed the maximum allowed
        if len(player_one_projectiles) < MAX_PROJCT:
            # Create a new projectile object starting from Player One's position
            projectile = Projectile(
                x=player_one.x
                + player_one.width,  # Start at the right edge of Player One
                y=player_one.y
                + player_one.height // 2
                - 2,  # Centered vertically on Player One
                velocity=PROJCT_VEL,  # Set the projectile's velocity
                image=PLAYER_ONE_PROJECTILE,  # Assign the image for Player One's projectile
            )
            # Add the new projectile to Player One's projectile list
            player_one_projectiles.append(projectile)
            # Play the shooting sound effect for Player One
            gameSound.play_player_one_fire()


def handle_player_two_shooting(event, player_two, player_two_projectiles):
    """
    Handle shooting logic for Player Two.

    Parameters:
    event (pygame.Event): The event triggering shooting.
    player_two (pygame.Rect): Player Two's rectangle object.
    player_two_projectiles (list): List of Player Two's projectiles.

    Returns:
    None
    """
    # Check if the event is a key press and if the 'M' key was pressed
    if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
        # Ensure the number of projectiles does not exceed the maximum allowed
        if len(player_two_projectiles) < MAX_PROJCT:
            # Create a new projectile object starting from Player Two's position
            projectile = Projectile(
                x=player_two.x,  # Start at the left edge of Player Two
                y=player_two.y
                + player_two.height // 2
                - 2,  # Centered vertically on Player Two
                velocity=-PROJCT_VEL,  # Set the projectile's velocity to move in the opposite direction
                image=PLAYER_TWO_PROJECTILE,  # Assign the image for Player Two's projectile
            )
            # Add the new projectile to Player Two's projectile list
            player_two_projectiles.append(projectile)
            # Play the shooting sound effect for Player Two
            gameSound.play_player_two_fire()


def handle_projectiles(
    player_one_projectiles, player_two_projectiles, player_one, player_two
):
    """
    Move projectiles, check collisions, and clean up off-screen projectiles.

    Parameters:
    player_one_projectiles (list): List of Player One's projectiles.
    player_two_projectiles (list): List of Player Two's projectiles.
    player_one (pygame.Rect): Player One's rectangle object.
    player_two (pygame.Rect): Player Two's rectangle object.

    Returns:
    None
    """
    # we will move each projectile in each player's list of fired projectiles and check for collision,
    # if the projectile hits the player it will be removed from the active list of projectiles,
    # like wise for projectiles that have moved outside of the dimensions of the screen
    # two similar functions are necessary since we need to maintain and update two different lists of projectiles, one for each player
    for projectile in player_one_projectiles[:]:
        projectile.move()
        if projectile.check_collision(player_two):
            pygame.event.post(pygame.event.Event(PLAYER_TWO_HIT))
            player_one_projectiles.remove(projectile)
        elif projectile.is_off_screen(WIDTH):
            player_one_projectiles.remove(projectile)

    for projectile in player_two_projectiles[:]:
        projectile.move()
        if projectile.check_collision(player_one):
            pygame.event.post(pygame.event.Event(PLAYER_ONE_HIT))
            player_two_projectiles.remove(projectile)
        elif projectile.is_off_screen(WIDTH):
            player_two_projectiles.remove(projectile)
