import pygame
import os

"""Encapsulate all of the game's functions relating to sound into one class"""

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.bullet_hit_sound = pygame.mixer.Sound(os.path.join('Assets', 'hitsound.wav'))
        self.player_one_fire_sound = pygame.mixer.Sound(os.path.join('Assets', 'player1ff.wav'))
        self.player_two_fire_sound = pygame.mixer.Sound(os.path.join('Assets', 'player2ff.wav'))
        self.background_music = pygame.mixer.Sound(os.path.join('Assets', 'background_music.mp3'))

    def play_hit_sound(self):
        self.bullet_hit_sound.play()  

    def play_player_one_fire(self):
        self.player_one_fire_sound.play()  

    def play_player_two_fire(self):
        self.player_two_fire_sound.play()  

    def play_background_music(self):
        self.background_music.play(-1) 
