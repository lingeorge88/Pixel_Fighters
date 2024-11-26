import pygame
from settings import FPS
from helpers import draw_window
from movement_logic import yellow_handle_movement, red_handle_movement
from game_objects import create_character_positions

def main():
    red, yellow = create_character_positions()
    clock = pygame.time.Clock()
    # Need to have the game running as long as we don't reach the win condition:
    # Use clock to cap how many times the while loop executes (60 times per second)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT
            ):  # if user closes the window, we terminate the game
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
