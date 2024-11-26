from settings import WIN, WHITE, BLACK, BORDER, RESIZE_YELLOW_SPACESHIP, RESIZE_RED_SPACESHIP
import pygame
"""
This is a the file that handles various helper functions like building the game background, drawing characters images on the screen, etc
"""
def draw_window(red, yellow):
    WIN.fill((WHITE))  # Setting up back ground color
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(RESIZE_YELLOW_SPACESHIP, (yellow.x, yellow.y)) # position the image, using x,y coordinates
    WIN.blit(RESIZE_RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()