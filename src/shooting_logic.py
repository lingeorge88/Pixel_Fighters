import pygame
from settings import MAX_BULLETS, WIDTH, BULLET_VEL, YELLOW_HIT, RED_HIT
from game_sound import SoundManager

gameSound = SoundManager()

"""Handles shooting logic in the game"""

def handle_yellow_shooting(event, yellow, yellow_bullets):
    """
    Handles shooting logic for the yellow spaceship.
    """
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q and len(yellow_bullets) < MAX_BULLETS:
            bullet = pygame.Rect(
                yellow.x + yellow.width, 
                yellow.y + yellow.height // 2 - 2, 
                10, 5
            )
            yellow_bullets.append(bullet)
            gameSound.play_player_one_fire()
def handle_red_shooting(event, red, red_bullets):
    """
    Handles shooting logic for the red spaceship.
    """
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_m and len(red_bullets) < MAX_BULLETS:
            bullet = pygame.Rect(
                red.x, 
                red.y + red.height // 2 - 2, 
                10, 5
            )
            red_bullets.append(bullet)
            gameSound.play_player_two_fire()


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)