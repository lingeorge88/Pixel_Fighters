import unittest
import pygame
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from projectile import Projectile


class TestProjectile(unittest.TestCase):
    def setUp(self):
        """
        Set up a default Projectile instance for testing.
        """
        self.projectile = Projectile(
            x=100, y=200, velocity=10, image=pygame.Surface((10, 10))
        )

    def test_projectile_movement(self):
        """
        Test that the projectile moves correctly based on its velocity.
        """
        initial_x = self.projectile.rect.x
        self.projectile.move()
        self.assertEqual(self.projectile.rect.x, initial_x + 10)

    def test_is_offscreen(self):
        """
        Test that the projectile is correctly identified as off-screen.
        """
        screen_width = 500
        self.assertEqual(
            self.projectile.is_off_screen(screen_width), False
        )  # Still on screen
        self.projectile.rect.x = 600  # Move off-screen
        self.assertEqual(
            self.projectile.is_off_screen(screen_width), True
        )  # Off-screen

    def test_check_collision(self):
        """
        Test that the projectile correctly detects collisions with a target.
        """
        target = pygame.Rect(100, 200, 50, 50)  # Target overlapping the projectile
        self.assertEqual(self.projectile.check_collision(target), True)
        target.x = 200  # Move target out of collision range
        self.assertEqual(self.projectile.check_collision(target), False)


if __name__ == "__main__":
    unittest.main()
