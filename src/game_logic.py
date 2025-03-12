"""
Implement hit detection and handling, and winning conditions for the game

This file contains the following functions:
- handle_hits: Handle hit events to update health and play sounds.
- check_winner: Determine if a player has won and handle appropriate logic (display text, menu options to exit or restart the game).
"""

import pygame
from helpers import draw_winner, restart_prompt
from settings import PLAYER_TWO_HIT, PLAYER_ONE_HIT


def handle_hits(event, player_two_health, player_one_health, sound_manager):
    """
    Handle hit events to update health and play sounds.

    Parameters:
    event (pygame.Event): The event triggering the hit.
    player_two_health (int): Health of Player Two.
    player_one_health (int): Health of Player One.
    sound_manager (SoundManager): Instance to play sound effect when a player is hit.

    Returns:
    tuple: Updated health values for Player Two and Player One.
    """
    # deducts health and plays hit sound when player two is hit
    if event.type == PLAYER_TWO_HIT:
        player_two_health -= 1
        sound_manager.play_hit_sound()
    # deducts health and plays hit sound when player one is hit
    if event.type == PLAYER_ONE_HIT:
        player_one_health -= 1
        sound_manager.play_hit_sound()
    return player_two_health, player_one_health


def check_winner(
    player_two_health,
    player_one_health,
    player_two,
    player_one,
    player_two_projectiles,
    player_one_projectiles,
):
    """
    Check if a winner exists and handle the winner logic.

    Returns:
        winner_text: A string indicating the winner, or an empty string if no winner yet.
    """
    # displays appropriate message based on the winner of the game
    winner_text = ""
    if player_two_health <= 0:
        winner_text = "PLAYER ONE Wins!"
    if player_one_health <= 0:
        winner_text = "PLAYER TWO Wins!"

    # display the restart prompt
    if winner_text != "":
        draw_winner(winner_text)
        if restart_prompt(
            player_two,
            player_one,
            player_two_projectiles,
            player_one_projectiles,
            player_two_health,
            player_one_health,
        ):
            return "RESTART"
    return winner_text
