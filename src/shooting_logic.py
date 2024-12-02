import pygame
from settings import PROJCT_VEL, MAX_PROJCT, WIDTH, PLAYER_ONE_HIT, PLAYER_TWO_HIT, PLAYER_ONE_PROJECTILE, PLAYER_TWO_PROJECTILE
from game_sound import SoundManager
from projectile import Projectile

gameSound = SoundManager()

"""Handles shooting logic in the game"""

def handle_player_one_shooting(event, player_one, player_one_projectiles):
    """
    Handles shooting logic for player 1.
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
        if len(player_one_projectiles) < MAX_PROJCT:
            projectile = Projectile(
                x=player_one.x + player_one.width,
                y=player_one.y + player_one.height // 2 - 2,
                width=10,
                height=17,
                velocity= PROJCT_VEL,
                image=PLAYER_ONE_PROJECTILE,
            )
            player_one_projectiles.append(projectile)
            gameSound.play_player_one_fire()

def handle_player_two_shooting(event, player_two, player_two_projectiles):
    """
    Handles shooting logic for player 2
    """
    if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
        if len(player_two_projectiles) < MAX_PROJCT:
            projectile = Projectile(
                x=player_two.x,
                y=player_two.y + player_two.height // 2 - 2,
                width=10,
                height=17,
                velocity= - PROJCT_VEL,
                image=PLAYER_TWO_PROJECTILE,
            )
            player_two_projectiles.append(projectile)
            gameSound.play_player_two_fire()

def handle_projectiles(player_one_projectiles, player_two_projectiles, player_one, player_two):
    """
    Move projectiles, check for collisions, and remove off-screen projectiles.
    """
    for projectile in player_one_projectiles[:]:
        projectile.move()
        if projectile.check_collision(player_two):
            pygame.event.post(pygame.event.Event(PLAYER_TWO_HIT))
            player_one_projectiles.remove(projectile)
        elif projectile.is_off_screen(WIDTH):
            player_one_projectiles.remove(projectile)

    for projectile in player_two_projectiles[:]:
        projectile.move()
        if projectile.check_collision(player_one):
            pygame.event.post(pygame.event.Event(PLAYER_ONE_HIT))
            player_two_projectiles.remove(projectile)
        elif projectile.is_off_screen(WIDTH):
            player_two_projectiles.remove(projectile)
