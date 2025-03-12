"""
This file contains global variables that will be reused throughout various other functions, can be viewed as the settings of the game
"""

import pygame
import os

# initialize pygame's font module to render and display game texts
pygame.font.init()

# Set up the size of the game window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Naming our game window and differentiating from default window name
pygame.display.set_caption("Pixel Fighter 1.0")

# Use tuples to store colors' RBG values for use later
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60  # How often our screen refreshes
VEL = 5  # Sets how fast the character moves
player_two_projectiles = (
    []
)  # a list used to keep track of player's one fired projectiles
player_one_projectiles = (
    []
)  # a list used to keep track of player's two fired projectiles
PROJCT_VEL = 8  # How fast the projectile that player shoots moves
MAX_PROJCT = 5  # Max bullets that can appear on each side at one time
CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT = 65, 90  # Scale for our character images
# We need to load character images and resize them
PLAYER_ONE_IMAGE = pygame.image.load(os.path.join("Assets", "char1.1.png"))
RESIZE_PLAYER_ONE = pygame.transform.scale(
    PLAYER_ONE_IMAGE, (CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT)
)
PLAYER_TWO_IMAGE = pygame.image.load(os.path.join("Assets", "char2.0.png"))
RESIZE_PLAYER_TWO = pygame.transform.scale(
    PLAYER_TWO_IMAGE, (CHARACTER_IMAGE_WIDTH, CHARACTER_IMAGE_HEIGHT)
)
# loading projectile images and resize them
PLAYER_ONE_PROJECTILE_IMAGE = pygame.image.load(
    os.path.join("Assets", "yellowPRJT.png")
)
PLAYER_TWO_PROJECTILE_IMAGE = pygame.image.load(os.path.join("Assets", "redPRJT.png"))

# rotate each projectile so they are oriented correctly
PLAYER_ONE_PROJECTILE = pygame.transform.rotate(
    pygame.transform.scale(PLAYER_ONE_PROJECTILE_IMAGE, (12, 21)), 90
)
PLAYER_TWO_PROJECTILE = pygame.transform.rotate(
    pygame.transform.scale(PLAYER_TWO_PROJECTILE_IMAGE, (12, 21)), 90
)

# load and sets the size of our background image
BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "background3.0.jpg")), (WIDTH, HEIGHT)
)

# Sets the border in the middle of the screen that players cannot move across
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

# Use pygame's USEREVENT constant to differentiate between different types of custom events, here it will be used to handle the logic when a player is hit by a projectile
PLAYER_ONE_HIT = pygame.USEREVENT + 1
PLAYER_TWO_HIT = pygame.USEREVENT + 2

# sets each players' starting health
player_one_health = 10
player_two_health = 10
# Various font sizes for different game texts
HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 90)
CONTROL_FONT = pygame.font.SysFont("comicsans", 20)
TITLE_FONT = pygame.font.SysFont("comicsans", 80)
