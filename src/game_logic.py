import pygame

from helpers import draw_winner, restart_prompt
from settings import RED_HIT, YELLOW_HIT

def handle_hits(event, red_health, yellow_health, sound_manager):
    """
    Handle RED_HIT and YELLOW_HIT events to update health and play hit sound.
    """
    if event.type == RED_HIT:
        red_health -= 1
        sound_manager.play_hit_sound()
    if event.type == YELLOW_HIT:
        yellow_health -= 1
        sound_manager.play_hit_sound()
    return red_health, yellow_health

def check_winner(red_health, yellow_health, red, yellow, red_bullets, yellow_bullets):
    """
    Check if a winner exists and handle the winner logic.

    Returns:
        winner_text: A string indicating the winner, or an empty string if no winner yet.
    """
    winner_text = ""
    if red_health <= 0:
        winner_text = "Yellow Wins!"
    if yellow_health <= 0:
        winner_text = "Red Wins!"

    if winner_text != "":
        draw_winner(winner_text)
        if restart_prompt(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
            return "RESTART"
    return winner_text