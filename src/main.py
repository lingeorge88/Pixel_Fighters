"""
Run the main game loop and manage high-level game operations.

This file contains the following functions:
- main: Run the main game loop.
"""

# We first need to import all the global variables and all necessary functions from other files that contain important game functions
import pygame
from settings import (
    FPS,
    player_one_projectiles,
    player_two_projectiles,
    player_two_health,
    player_one_health,
    WIN,
)
from helpers import draw_window, render_projectiles
from movement_logic import player_one_handle_movement, player_two_handle_movement
from game_objects import create_character_positions
from shooting_logic import (
    handle_player_one_shooting,
    handle_player_two_shooting,
    handle_projectiles,
)
from game_logic import handle_hits, check_winner
from game_sound import SoundManager
from title_screen import menu_options

# create an instance of the SoundManager class to pass into functions that require it so game sounds may be played
game_sounds = SoundManager()


def main():
    """
    Run the main game loop.

    Parameters:
    None

    Returns:
    None
    """

    # Reset health values for both players at the start of the game
    global player_two_health, player_one_health  # Ensure global variables are reset
    player_two_health = 10  # player two starts with 10 health points
    player_one_health = 10  # player one starts with 10 health points
    # Clear any projectiles from previous games / sessions
    player_one_projectiles.clear()
    player_two_projectiles.clear()

    # Create the initial positions for player One and Two's characters
    player_two, player_one = create_character_positions()
    # Initialize the pygame Clock object to control the frame rate of the game
    clock = pygame.time.Clock()
    # Set the main game loop to run until the game is exited
    run = True
    while run:
        # limit the loop to run at the specified frames per second (60)
        clock.tick(FPS)
        # Use pygame's event module to process / handle all events (e.g. keyboard, mouse, game window, etc.)
        for event in pygame.event.get():
            # if user closes the window, we exit the game loop so the game does not run in the background
            if event.type == pygame.QUIT:
                run = False
            # Handle player one's shooting logic
            handle_player_one_shooting(event, player_one, player_one_projectiles)
            # handle player two's shooting logic
            handle_player_two_shooting(event, player_two, player_two_projectiles)
            # update each player's health points if either player is hit by a projectile
            player_two_health, player_one_health = handle_hits(
                event, player_two_health, player_one_health, game_sounds
            )

        # check for winner and display corresponding messages and restarts / quits the game based on input
        winner = check_winner(
            player_two_health,
            player_one_health,
            player_two,
            player_one,
            player_two_projectiles,
            player_one_projectiles,
        )
        # Check for all of the keys pressed to handle appropriate action on the game screen
        keys_pressed = pygame.key.get_pressed()

        # Handle movement for both players' characters based on key input
        player_one_handle_movement(keys_pressed, player_one)
        player_two_handle_movement(keys_pressed, player_two)
        handle_projectiles(
            player_one_projectiles, player_two_projectiles, player_one, player_two
        )
        # Draw the game window (characters, projectiles, health bars, texts, etc.)
        draw_window(
            player_two,
            player_one,
            player_two_projectiles,
            player_one_projectiles,
            player_two_health,
            player_one_health,
        )
        # render projectiles on the screen
        render_projectiles(player_one_projectiles, player_two_projectiles, WIN)

        # Update the game screen to reflect any changes
        pygame.display.update()

        # Restart the game if the previous check_winner() function indicates a restart
        if winner == "RESTART":
            main()
            break
    # quit the game once the main loop ends
    pygame.quit()


# Entry point for our game
if __name__ == "__main__":
    # Play background music in a loop
    game_sounds.play_background_music()

    # Display the game's title screen with menu options
    menu_options()

    # Start the main game loop
    main()
