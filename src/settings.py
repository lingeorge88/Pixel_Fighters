import pygame
import os
pygame.font.init()
"""This is the settings file that specifies window size, sizes of images, colors, etc, for the game"""
"""
Set up the size of the window
"""
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(
    "Pixel Fighter 1.0"
)  # Naming our game window and differentiating from default window name
# Setting up event loop in Pygame
WHITE = (255, 255, 255)  # Setting up back ground color
BLACK = (0, 0, 0) # Border color
RED = (255, 0 ,0)
YELLOW = (255, 255, 0)
FPS = 60 # How often our screen refreshes
VEL = 5 # SETS how fast space ship moves
red_bullets = []
yellow_bullets = []
BULLET_VEL = 8 # how fast the bullet that player shoots moves
MAX_BULLETS = 5 # max bullets that can appear on each side at one time
CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT = 55, 40 # scale for our character images
# We need to load character images and resize them
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", 'spaceship_yellow.png')) 
RESIZE_YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", 'spaceship_red.png'))
RESIZE_RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT)), 270)

BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space.png")), (WIDTH, HEIGHT))
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)  # Sets the border in the middle of the screen .

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

yellow_health = 10
red_health = 10
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
MENU_FONT = pygame.font.SysFont('comicsans', 40)