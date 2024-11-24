import pygame

"""
Set up the size of the window
"""
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

"""Setting up event loop in Pygame"""


def main():
    # Need to have the game running as long as we don't reach the win condition:
    run = True
    while run:

        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT
            ):  # if user closes the window, we terminate the game
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()
