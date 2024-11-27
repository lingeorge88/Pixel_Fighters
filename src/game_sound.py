import pygame
import os

pygame.mixer.init()

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'hitsound.wav'))
PLAYER_ONE_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'player1ff.wav'))
PLAYER_TWO_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'player2ff.wav'))
BACKGROUND_MUSIC = pygame.mixer.Sound(os.path.join('Assets', 'background_music.mp3'))


def player_one_fire_sound():
    PLAYER_ONE_FIRE_SOUND.play()

def player_two_fire_sound():
    PLAYER_TWO_FIRE_SOUND.play()

def play_hit_sound():
    BULLET_HIT_SOUND.play()

def play_background_music():
    BACKGROUND_MUSIC.play(-1)