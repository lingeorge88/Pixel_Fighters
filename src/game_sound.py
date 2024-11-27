import pygame
import os

pygame.mixer.init()

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

def play_fire_sound():
    BULLET_FIRE_SOUND.play()

def play_hit_sound():
    BULLET_HIT_SOUND.play()