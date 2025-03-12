import unittest
import pygame
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from shooting_logic import handle_projectiles
from projectile import Projectile
from settings import (
    PLAYER_ONE_PROJECTILE,
    PLAYER_TWO_PROJECTILE,
    PLAYER_ONE_HIT,
    PLAYER_TWO_HIT,
    WIDTH,
)


class TestHandleProjectiles(unittest.TestCase):
    def setUp(self):
        """
        Set up the players and projectile lists for testing projectile handling.
        """
        self.player_one = pygame.Rect(50, 50, 50, 50)  # Player One's rectangle
        self.player_two = pygame.Rect(700, 50, 50, 50)  # Player Two's rectangle

        # Create actual Projectile instances
        self.player_one_projectiles = [
            Projectile(
                x=100,
                y=75,
                velocity=10,
                image=PLAYER_ONE_PROJECTILE,
            )
        ]
        self.player_two_projectiles = [
            Projectile(
                x=WIDTH - 150,
                y=75,
                velocity=-10,
                image=PLAYER_TWO_PROJECTILE,
            )
        ]

    def test_projectiles_move(self):
        """
        Test that projectiles move correctly.
        """
        handle_projectiles(
            self.player_one_projectiles,
            self.player_two_projectiles,
            self.player_one,
            self.player_two,
        )

        # Assert that projectiles have moved
        self.assertEqual(self.player_one_projectiles[0].rect.x, 110)  # 100 + 10
        self.assertEqual(
            self.player_two_projectiles[0].rect.x, WIDTH - 160
        )  # WIDTH-150 - 10

    def test_projectiles_check_collision_player_two(self):
        """
        Test that collisions are handled correctly for projectiles.
        """
        # Move Player ONE to ensure collision
        self.player_one.x = WIDTH - 140
        self.player_one.y = 75

        handle_projectiles(
            self.player_one_projectiles,
            self.player_two_projectiles,
            self.player_one,
            self.player_two,
        )

        # Assert that Player Two's projectile was removed after collision
        self.assertEqual(len(self.player_two_projectiles), 0)

    def test_projectiles_check_collision_player_one(self):
        """
        Test that collisions are handled correctly for projectiles.
        """
        # Move Player TWO to ensure collision with player ONE's projectiles
        self.player_two.x = 110
        self.player_two.y = 75

        handle_projectiles(
            self.player_one_projectiles,
            self.player_two_projectiles,
            self.player_one,
            self.player_two,
        )

        # Assert that Player Two's projectile was removed after collision
        self.assertEqual(len(self.player_one_projectiles), 0)

    def test_projectiles_check_off_screen(self):
        """
        Test that off-screen projectiles are removed correctly.
        """
        # Move Player One's projectile off-screen
        self.player_one_projectiles[0].rect.x = WIDTH + 1

        handle_projectiles(
            self.player_one_projectiles,
            self.player_two_projectiles,
            self.player_one,
            self.player_two,
        )

        # Assert that the off-screen projectile was removed
        self.assertEqual(len(self.player_one_projectiles), 0)

    def test_no_collision_or_off_screen(self):
        """
        Test that projectiles remain when there are no collisions or off-screen events.
        """
        handle_projectiles(
            self.player_one_projectiles,
            self.player_two_projectiles,
            self.player_one,
            self.player_two,
        )

        # Assert that projectiles remain in the list
        self.assertEqual(len(self.player_one_projectiles), 1)
        self.assertEqual(len(self.player_two_projectiles), 1)


if __name__ == "__main__":
    unittest.main()
