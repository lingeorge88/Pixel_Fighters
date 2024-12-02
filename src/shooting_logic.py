import pygame
from settings import MAX_BULLETS, WIDTH, BULLET_VEL, PLAYER_ONE_HIT, PLAYER_TWO_HIT, PLAYER_ONE_PROJECTILE, PLAYER_TWO_PROJECTILE
from game_sound import SoundManager
from bullet import Bullet

gameSound = SoundManager()

"""Handles shooting logic in the game"""

def handle_player_one_shooting(event, player_one, player_one_bullets):
    """
    Handles shooting logic for player 1.
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
        if len(player_one_bullets) < MAX_BULLETS:
            bullet = Bullet(
                x=player_one.x + player_one.width,
                y=player_one.y + player_one.height // 2 - 2,
                width=10,
                height=17,
                velocity=BULLET_VEL,
                image=PLAYER_ONE_PROJECTILE,
            )
            player_one_bullets.append(bullet)
            gameSound.play_player_one_fire()

def handle_player_two_shooting(event, player_two, player_two_bullets):
    """
    Handles shooting logic for player 2
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
        if len(player_two_bullets) < MAX_BULLETS:
            bullet = Bullet(
                x=player_two.x,
                y=player_two.y + player_two.height // 2 - 2,
                width=10,
                height=17,
                velocity=-BULLET_VEL,
                image=PLAYER_TWO_PROJECTILE,
            )
            player_two_bullets.append(bullet)
            gameSound.play_player_two_fire()

def handle_bullets(player_one_bullets, player_two_bullets, player_one, player_two):
    """
    Move bullets, check for collisions, and remove off-screen bullets.
    """
    for bullet in player_one_bullets[:]:
        bullet.move()
        if bullet.check_collision(player_two):
            pygame.event.post(pygame.event.Event(PLAYER_TWO_HIT))
            player_one_bullets.remove(bullet)
        elif bullet.is_off_screen(WIDTH):
            player_one_bullets.remove(bullet)

    for bullet in player_two_bullets[:]:
        bullet.move()
        if bullet.check_collision(player_one):
            pygame.event.post(pygame.event.Event(PLAYER_ONE_HIT))
            player_two_bullets.remove(bullet)
        elif bullet.is_off_screen(WIDTH):
            player_two_bullets.remove(bullet)
