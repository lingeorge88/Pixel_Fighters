"""
Provide utility functions for rendering and game assistance.

This file contains the following functions:
- draw_window: Render the game window with updated visuals.
- draw_winner: Display the winner text in the game window.
- render_projectiles: Render projectiles for both players.
- restart_prompt: Prompt the player to restart or quit the game.
"""

from settings import (
    FPS,
    WIN,
    WHITE,
    BLACK,
    BORDER,
    BACKGROUND_IMAGE,
    HEALTH_FONT,
    WIDTH,
    WINNER_FONT,
    HEIGHT,
    RESIZE_PLAYER_ONE,
    RESIZE_PLAYER_TWO,
)
import pygame


def draw_window(
    player_two,
    player_one,
    player_two_projectiles,
    player_one_projectiles,
    player_two_health,
    player_one_health,
):
    """
    Render the game window with updated visuals.

    Parameters:
    player_two (pygame.Rect): Player Two's rectangle object.
    player_one (pygame.Rect): Player One's rectangle object.
    player_two_projectiles (list): List of Player Two's projectiles.
    player_one_projectiles (list): List of Player One's projectiles.
    player_two_health (int): Health of Player Two.
    player_one_health (int): Health of Player One.

    Returns:
    None
    """
    WIN.blit((BACKGROUND_IMAGE), (0, 0))  # Setting up back ground
    pygame.draw.rect(WIN, BLACK, BORDER)  # Draw a border that the players can't cross
    # Set the texts to display on the screen
    player_two_health_text = HEALTH_FONT.render(
        "Health: " + str(player_two_health), 1, WHITE
    )
    player_one_health_text = HEALTH_FONT.render(
        "Health: " + str(player_one_health), 1, WHITE
    )
    # Specify where to render the Health status text for each player
    WIN.blit(
        player_two_health_text, (WIDTH - player_two_health_text.get_width() - 10, 10)
    )
    WIN.blit(player_one_health_text, (10, 10))
    # render player character images and
    WIN.blit(RESIZE_PLAYER_ONE, (player_one.x, player_one.y))
    WIN.blit(RESIZE_PLAYER_TWO, (player_two.x, player_two.y))
    # update the game display for renders to show
    pygame.display.update()


def draw_winner(text):
    """
    Display the winner text in the game window.

    Parameters:
    text (str): The winner message to display.

    Returns:
    None
    """
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(
        draw_text,
        (
            WIDTH / 2 - draw_text.get_width() / 2,
            HEIGHT / 2 - draw_text.get_height() / 2,
        ),
    )
    pygame.display.update()
    # .delay () function controls how long the text appears on the screen for, before proceeding to the next rendering
    pygame.time.delay(3000)


def render_projectiles(player_one_projectiles, player_two_projectiles, WIN):
    """
    Render projectiles for both players with each project object's draw method

    Parameters:
    player_one_projectiles (list): List of Player One's projectiles.
    player_two_projectiles (list): List of Player Two's projectiles.
    WIN (pygame.Surface): The game window surface.

    Returns:
    None
    """
    for projectile in player_one_projectiles:
        projectile.draw(
            WIN
        )  # Use the projectile class's draw method to render the image for each projectile that is fired (player one)
    for projectile in player_two_projectiles:
        projectile.draw(
            WIN
        )  # Use the projectile class's draw method to render the image for player two as well


def restart_prompt(
    player_two,
    player_one,
    player_two_projectiles,
    player_one_projectiles,
    player_two_health,
    player_one_health,
):
    """
    Prompt the player to restart or quit the game.

    Parameters:
    player_two (pygame.Rect): Player Two's rectangle object.
    player_one (pygame.Rect): Player One's rectangle object.
    player_two_projectiles (list): List of Player Two's projectiles.
    player_one_projectiles (list): List of Player One's projectiles.
    player_two_health (int): Health of Player Two.
    player_one_health (int): Health of Player One.

    Returns:
    bool: True if restart is selected, exits the game otherwise.
    """
    WIN = pygame.display.get_surface()
    restart_text = HEALTH_FONT.render(
        "Press R to Restart or E to Exit the program", True, WHITE
    )
    clock = pygame.time.Clock()
    run = True
    # We will display the options of restarting or exiting the game as long as the game window has not been closed,
    # this loop executes at the specified FPS
    while run:
        # listen for all events (keyboard, mouse, etc.)
        for event in pygame.event.get():
            # if user closes game window then we stop the execution of the program
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart game with 'R' key
                    return True
                if event.key == pygame.K_e:  # Quit game with 'E' key
                    pygame.quit()
                    exit()
        clock.tick(FPS)
        # draw the game screen
        draw_window(
            player_two,
            player_one,
            player_two_projectiles,
            player_one_projectiles,
            player_two_health,
            player_one_health,
        )
        # we don't want the text to render at the same rate as the game's default FPS since that will make texts flash 60 times a second, so we delay the rendering for the texts each second at the restart menu
        if pygame.time.get_ticks() % 3200 < 2800:
            WIN.blit(
                restart_text,
                (
                    WIDTH // 2 - restart_text.get_width() // 2,
                    HEIGHT // 2 - restart_text.get_height() // 2,
                ),
            )

        pygame.display.update()
