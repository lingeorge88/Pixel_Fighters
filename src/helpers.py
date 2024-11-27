from settings import WIN, WHITE, BLACK, BORDER, RESIZE_YELLOW_SPACESHIP, RESIZE_RED_SPACESHIP, RED, YELLOW, red_bullets, yellow_bullets, BACKGROUND_IMAGE
import pygame
"""
This is a the file that handles various helper functions like building the game background, drawing characters images on the screen, etc
"""
def draw_window(red, yellow, red_bullets, yellow_bullets):
    WIN.blit((BACKGROUND_IMAGE), (0, 0))  # Setting up back ground color
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(RESIZE_YELLOW_SPACESHIP, (yellow.x, yellow.y)) # position the image, using x,y coordinates
    WIN.blit(RESIZE_RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    pygame.display.update()