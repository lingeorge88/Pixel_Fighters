import unittest
import pygame
from unittest.mock import MagicMock, patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from shooting_logic import handle_player_one_shooting, handle_player_two_shooting
from projectile import Projectile
from settings import PROJCT_VEL


class TestShootingLogic(unittest.TestCase):
    def setUp(self):
        """
        Set up dummy objects for testing shooting logic.
        """
        self.player_one = pygame.Rect(50, 50, 50, 50)  # Player One's rectangle
        self.player_two = pygame.Rect(700, 50, 50, 50)  # Player Two's rectangle
        self.player_one_projectiles = []
        self.player_two_projectiles = []
        self.projct_vel = PROJCT_VEL  # Match PROJCT_VEL from settings

    def test_handle_player_one_shooting(self):
        """
        Test that Player One shoots a projectile when the correct key is pressed.
        """
        # Simulate KEYDOWN event for shooting
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_q)
        handle_player_one_shooting(event, self.player_one, self.player_one_projectiles)

        # Assert a projectile is added to the list
        self.assertEqual(len(self.player_one_projectiles), 1)
        projectile = self.player_one_projectiles[0]
        self.assertIsInstance(projectile, Projectile)
        self.assertEqual(projectile.rect.x, self.player_one.x + self.player_one.width)
        self.assertEqual(projectile.velocity, self.projct_vel)

    def test_handle_player_two_shooting(self):
        """
        Test that Player Two shoots a projectile when the correct key is pressed.
        """
        # Simulate KEYDOWN event for shooting
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_m)
        handle_player_two_shooting(event, self.player_two, self.player_two_projectiles)

        # Assert a projectile is added to the list
        self.assertEqual(len(self.player_two_projectiles), 1)
        projectile = self.player_two_projectiles[0]
        self.assertIsInstance(projectile, Projectile)
        self.assertEqual(projectile.rect.x, self.player_two.x)
        self.assertEqual(projectile.velocity, -self.projct_vel)


if __name__ == "__main__":
    unittest.main()
