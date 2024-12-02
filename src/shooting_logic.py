import pygame
from settings import MAX_BULLETS, WIDTH, BULLET_VEL, YELLOW_HIT, RED_HIT, PLAYER_ONE_PROJECTILE, PLAYER_TWO_PROJECTILE
from game_sound import SoundManager
from bullet import Bullet

gameSound = SoundManager()

"""Handles shooting logic in the game"""

def handle_yellow_shooting(event, yellow, yellow_bullets):
    """
    Handles shooting logic for player 1.
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
        if len(yellow_bullets) < MAX_BULLETS:
            bullet = Bullet(
                x=yellow.x + yellow.width,
                y=yellow.y + yellow.height // 2 - 2,
                width=10,
                height=17,
                velocity=BULLET_VEL,
                image=PLAYER_ONE_PROJECTILE,
            )
            yellow_bullets.append(bullet)
            gameSound.play_player_one_fire()
def handle_red_shooting(event, red, red_bullets):
    """
    Handles shooting logic for player 2
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
        if len(red_bullets) < MAX_BULLETS:
            bullet = Bullet(
                x=red.x,
                y=red.y + red.height // 2 - 2,
                width=10,
                height=17,
                velocity=-BULLET_VEL,
                image = PLAYER_TWO_PROJECTILE
            )
            red_bullets.append(bullet)
            gameSound.play_player_two_fire()


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    """
    Move bullets, check for collisions, and remove off-screen bullets.
    """
    for bullet in yellow_bullets[:]:
        bullet.move()
        if bullet.check_collision(red):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.is_off_screen(WIDTH):
            yellow_bullets.remove(bullet)

    for bullet in red_bullets[:]:
        bullet.move()
        if bullet.check_collision(yellow):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.is_off_screen(WIDTH):
            red_bullets.remove(bullet)