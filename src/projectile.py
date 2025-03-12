"""
Define the Projectile class and its associated methods.

This file contains the following functions:
- __init__: Initialize a projectile with its properties.
- move: Update the projectile's position.
- is_off_screen: Check if the projectile has moved off the screen.
- check_collision: Check if the projectile collides with a target.
- draw: Render the projectile on the game window.
"""

import pygame


class Projectile:
    def __init__(self, x, y, velocity, image):
        """
        Initialize a projectile object.

        Parameters:
        - x, y: Starting position of the projectile
        - image: image of the projectile
        - velocity: how fast the projectile moves (positive for right, negative for left).
        """
        self.image = image
        # .get_rect method aligns each projectile's top left corner with the character's position
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity = velocity

    def move(self):
        """Update the projectile's position based on its velocity.

        Parameters:
        None

        Returns:
        None"""
        # the projectile will move horizontally at the specified velocity each time it moves
        self.rect.x += self.velocity

    def is_off_screen(self, screen_width):
        """
        Check if the projectile has moved off the screen.

        Parameters:
        screen_width (int): The width of the game screen.

        Returns:
        bool: True if the projectile is off-screen, False otherwise.
        """
        # check to see if the projectile has moved off screen with the specified dimensions of the game screen
        return self.rect.x < 0 or self.rect.x > screen_width

    def check_collision(self, target_rect):
        """
        Check if the projectile collides with a target.

        Parameters:
        target_rect (pygame.Rect): The target's rectangle for collision detection.

        Returns:
        bool: True if a collision is detected, False otherwise.
        """
        # use pygame's .colliderect() method to see if the projectile has collided with another pygame rect object
        return self.rect.colliderect(target_rect)

    def draw(self, win):
        """
        Render the projectile on the game window.

        Parameters:
        win (pygame.Surface): The game window surface.

        Returns:
        None
        """
        # render the projectile's image with the x,y coordinates using pygame's win.blit() method
        win.blit(self.image, (self.rect.x, self.rect.y))
