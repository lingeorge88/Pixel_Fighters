import pygame

from helpers import draw_winner, restart_prompt
from settings import PLAYER_TWO_HIT, PLAYER_ONE_HIT

def handle_hits(event, player_two_health, player_one_health, sound_manager):
    """
    Handle PLAYER_TWO_HIT and PLAYER_ONE_HIT events to update health and play hit sound.
    """
    if event.type == PLAYER_TWO_HIT:
        player_two_health -= 1
        sound_manager.play_hit_sound()
    if event.type == PLAYER_ONE_HIT:
        player_one_health -= 1
        sound_manager.play_hit_sound()
    return player_two_health, player_one_health

def check_winner(player_two_health, player_one_health, player_two, player_one, player_two_bullets, player_one_bullets):
    """
    Check if a winner exists and handle the winner logic.

    Returns:
        winner_text: A string indicating the winner, or an empty string if no winner yet.
    """
    winner_text = ""
    if player_two_health <= 0:
        winner_text = "PLAYER ONE Wins!"
    if player_one_health <= 0:
        winner_text = "PLAYER TWO Wins!"

    if winner_text != "":
        draw_winner(winner_text)
        if restart_prompt(player_two, player_one, player_two_bullets, player_one_bullets, player_two_health, player_one_health):
            return "RESTART"
    return winner_text
