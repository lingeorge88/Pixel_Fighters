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
WHITE = (255, 255, 255)  # Setting up background color
BLACK = (0, 0, 0)  # Border color
PLAYER_TWO = (255, 0, 0)
PLAYER_ONE = (255, 255, 0)
FPS = 60  # How often our screen refreshes
VEL = 5  # Sets how fast space ship moves
player_two_bullets = []
player_one_bullets = []
BULLET_VEL = 8  # How fast the bullet that player shoots moves
MAX_BULLETS = 5  # Max bullets that can appear on each side at one time
CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT = 65, 90  # Scale for our character images
# We need to load character images and resize them
PLAYER_ONE_IMAGE = pygame.image.load(os.path.join("Assets", 'char1.1.png'))
RESIZE_PLAYER_ONE = pygame.transform.scale(PLAYER_ONE_IMAGE, (CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT))
PLAYER_TWO_IMAGE = pygame.image.load(os.path.join("Assets", 'char2.0.png'))
RESIZE_PLAYER_TWO = pygame.transform.scale(PLAYER_TWO_IMAGE, (CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT))

PLAYER_ONE_PROJECTILE_IMAGE = pygame.image.load(os.path.join("Assets", "yellowPRJT.png"))
PLAYER_TWO_PROJECTILE_IMAGE = pygame.image.load(os.path.join("Assets", "redPRJT.png"))

PLAYER_ONE_PROJECTILE = pygame.transform.rotate(pygame.transform.scale(PLAYER_ONE_PROJECTILE_IMAGE, (12, 21)), 90)
PLAYER_TWO_PROJECTILE = pygame.transform.rotate(pygame.transform.scale(PLAYER_TWO_PROJECTILE_IMAGE, (12, 21)), 90)

BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "background3.0.jpg")), (WIDTH, HEIGHT))
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)  # Sets the border in the middle of the screen.

PLAYER_ONE_HIT = pygame.USEREVENT + 1
PLAYER_TWO_HIT = pygame.USEREVENT + 2

player_one_health = 10
player_two_health = 10
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
CONTROL_FONT = pygame.font.SysFont('comicsans', 20)
TITLE_FONT = pygame.font.SysFont('comicsans', 80)
