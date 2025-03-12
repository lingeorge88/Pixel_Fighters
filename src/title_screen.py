"""
Functions contained in this file manage the title and control screens for the game

- menu_options: Display the title screen with game options
- controls_screen: Display the instructions for each player for the game
"""

import pygame
from settings import (
    WIN,
    WIDTH,
    HEIGHT,
    WHITE,
    BACKGROUND_IMAGE,
    HEALTH_FONT,
    CONTROL_FONT,
    TITLE_FONT,
)


def menu_options():
    """
    Display the title screen with game options, players can either start the game or view the controls

    Parameters:
    None

    Returns:
    None
    """
    run = True
    while run:
        # render game's background image
        WIN.blit(BACKGROUND_IMAGE, (0, 0))

        # save strings in variables for rendering later. Texts are in white color
        title_text = TITLE_FONT.render("Pixel Fighter 1.0", True, WHITE)
        start_text = HEALTH_FONT.render("Start Game (Press S)", True, WHITE)
        controls_text = HEALTH_FONT.render("Controls (Press C)", True, WHITE)

        # Display the title and options with pygame's built-in blit function
        WIN.blit(title_text, ((WIDTH - title_text.get_width()) // 2, HEIGHT // 4))
        WIN.blit(start_text, ((WIDTH - start_text.get_width()) // 2, HEIGHT // 2))
        WIN.blit(
            controls_text, ((WIDTH - controls_text.get_width()) // 2, HEIGHT // 2 + 50)
        )
        # Update the game screen with texts
        pygame.display.update()

        # use for-loops to check for keyboard events or when user closes out of the program and performs associated actions appropriately
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if (
                    event.key == pygame.K_s
                ):  # Start the game if the user presses 'S' at the title screen
                    return
                if (
                    event.key == pygame.K_c
                ):  # Show controls if the user presses 'C' at the title screen
                    controls_screen()


def controls_screen():
    """
     Display the controls screen for player instructions. Players have the option to return to the title screen from here

    Parameters:
    None

    Returns:
    None
    """
    run = True
    line_spacing = 40  # Vertical space between lines
    margin = 50  # Left and right margin for text
    while run:
        WIN.blit(BACKGROUND_IMAGE, (0, 0))  # Render background image
        controls_title = CONTROL_FONT.render("Controls", True, WHITE)
        # Text that will be displayed on the controls screen
        controls_text = [
            "Player 1: W - Move Up, S - Move Down, A - Move Left, D - Move Right, Q - Shoot",
            "Player 2: Arrow Keys to Move, M - Shoot",
            "Press ESC to return to the title screen",
        ]

        # Render controls text
        WIN.blit(
            controls_title, ((WIDTH - controls_title.get_width()) // 2, HEIGHT // 4)
        )
        # render each line with a for-loop and add appropriate margin and vertical spacing
        for i, line in enumerate(controls_text):
            controls_line = CONTROL_FONT.render(line, True, WHITE)
            WIN.blit(controls_line, (margin, HEIGHT // 2 + i * line_spacing))

        pygame.display.update()

        # use for-loop to check for keyboard events or when user closes out of the program and performs associated actions appropriately
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if (
                    event.key == pygame.K_ESCAPE
                ):  # Give user the option to return to the title screen and start the game if necessary after pressing 'ESC' key
                    return
