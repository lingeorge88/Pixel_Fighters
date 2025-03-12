"""
Manage game sound effects and background music.

This file contains the following functions:
- __init__: Initialize sound effects and background music.
- play_hit_sound: Play the sound effect for a hit event.
- play_player_one_fire: Play the sound effect for Player One's projectile fire.
- play_player_two_fire: Play the sound effect for Player Two's projectile fire.
- play_background_music: Play the background music in a loop.
"""

import pygame
import os


class SoundManager:
    """
    Initialize sound effects with pygame's mixer module and load music associated file directories

    Parameters:
    None

    Returns:
    None
    """

    def __init__(self):
        pygame.mixer.init()
        self.projectile_hit_sound = pygame.mixer.Sound(
            os.path.join("Assets", "hitsound.wav")
        )  # load asset for sound of players being hit by projectile
        self.player_one_fire_sound = pygame.mixer.Sound(
            os.path.join("Assets", "player1ff.wav")
        )  # load sound asset of player one firing projectile
        self.player_two_fire_sound = pygame.mixer.Sound(
            os.path.join("Assets", "player2ff.wav")
        )  # load sound asset of player two firing projectile
        self.background_music = pygame.mixer.Sound(
            os.path.join("Assets", "background_music.mp3")
        )  # load sound asset for the background music of the game

        # Assign separate channels for Player One and Player Two firing sounds and hit sound
        self.player_one_channel = pygame.mixer.Channel(1)  # Channel 1 for Player One
        self.player_two_channel = pygame.mixer.Channel(2)  # Channel 2 for Player Two
        self.hit_sound_channel = pygame.mixer.Channel(3)  # Channel 3 for hit sound

    def play_hit_sound(self):
        """
        Play the sound effect for when a player gets hit.

        Parameters:
        None

        Returns:
        None
        """
        # Play the specified sound using the dedicated channel to avoid sounds overriding each other
        self.hit_sound_channel.play(self.projectile_hit_sound)

    def play_player_one_fire(self):
        """
        Play the sound effect for player one's projectile fire with pygame's built-in .play() method.

        Parameters:
        None

        Returns:
        None
        """
        # Play the specified sound using the dedicated channel to avoid sounds overriding each other
        self.player_one_channel.play(self.player_one_fire_sound)

    def play_player_two_fire(self):
        """
        Play the sound effect for player two's projectile fire with pygame's built-in .play() method.

        Parameters:
        None

        Returns:
        None
        """
        # Play the specified sound using the dedicated channel to avoid sounds overriding each other
        self.player_two_channel.play(self.player_two_fire_sound)

    def play_background_music(self):
        """
        Play the background music in a loop, pass in -1 to start a loop with pygame's built-in .play() method.

        Parameters:
        None

        Returns:
        None
        """
        # Play the background music in a loop
        self.background_music.play(-1)
