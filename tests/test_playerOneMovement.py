import unittest
import pygame
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from movement_logic import player_one_handle_movement
from settings import VEL, WIDTH, HEIGHT, BORDER


class MockKeys:
    """
    Mock pygame key presses for testing.
    """

    def __init__(self, keys):
        self.keys = keys

    def __getitem__(self, key):
        return self.keys.get(key, False)


class TestPlayerOneMovementLogic(unittest.TestCase):
    def setUp(self):
        """
        Set up game screen dimensions, initial player positions, and velocities.
        """
        self.screen_width = WIDTH  # Width of the game screen is 900
        self.screen_height = HEIGHT  # Height of the game screen is 500 pixels
        self.border = BORDER  # Border object from settings in the middle of the screen
        self.player_one = pygame.Rect(50, 50, 50, 50)  # Player One's rectangle
        self.velocity = VEL  # Player moves at 5 pixels per key press

    def test_player_one_move_left(self):
        """
        Test that Player One moves left within screen boundaries at the specified speed
        """
        keys_pressed = MockKeys({pygame.K_a: True})  # 'A' key pressed
        player_one_handle_movement(keys_pressed, self.player_one)
        self.assertEqual(self.player_one.x, 45)  # 50 - 5

    def test_player_one_move_right(self):
        """
        Test that Player One moves right within screen boundaries at the specified speed
        """
        keys_pressed = MockKeys({pygame.K_d: True})  # Mock 'D' key pressed
        player_one_handle_movement(keys_pressed, self.player_one)
        self.assertEqual(self.player_one.x, 55)  # 55 + 5

    def test_player_one_move_up(self):
        """
        Test that Player One moves up within screen boundaries at the specified speed
        """
        keys_pressed = MockKeys({pygame.K_w: True})  # Mock 'W' key pressed
        player_one_handle_movement(keys_pressed, self.player_one)
        self.assertEqual(self.player_one.y, 45)  # 50 - 5

    def test_player_one_move_down(self):
        """
        Test that Player One moves down within screen boundaries at the specified speed
        """
        keys_pressed = MockKeys({pygame.K_s: True})  # Mock 'S' key pressed
        player_one_handle_movement(keys_pressed, self.player_one)
        self.assertEqual(self.player_one.y, 55)  # 55 - 5

    def test_player_one_move_left_boundary(self):
        """
        Test that Player One does not move off the left boundary.
        """
        self.player_one.x = 0  # Already at the left boundary
        keys_pressed = MockKeys({pygame.K_a: True})  # 'A' key pressed
        player_one_handle_movement(keys_pressed, self.player_one)
        self.assertEqual(self.player_one.x, 0)  # Should stay at 0

    def test_player_one_move_right_boundary(self):
        """
        Test that Player One does not move off the right boundary(The border in the middle of the screen).
        """
        self.player_one.x = (
            self.border.x - self.player_one.width
        )  # At right edge of border
        keys_pressed = MockKeys({pygame.K_d: True})  # 'D' key pressed
        player_one_handle_movement(keys_pressed, self.player_one)
        self.assertEqual(
            self.player_one.x, self.border.x - self.player_one.width
        )  # Should stay at the left side of the border

    def test_player_one_move_up_boundary(self):
        """
        Test that Player One does not move off the top boundary.
        """
        self.player_one.y = 0  # Already at the top boundary
        keys_pressed = MockKeys({pygame.K_w: True})  # 'W' key pressed
        player_one_handle_movement(keys_pressed, self.player_one)
        self.assertEqual(self.player_one.y, 0)  # Should stay at 0

    def test_player_one_move_down_boundary(self):
        """
        Test that Player One does not move off the top boundary.
        """
        self.player_one.y = (
            self.screen_height - self.player_one.height
        )  # Already at the bottom boundary
        keys_pressed = MockKeys({pygame.K_s: True})  # 'S' key pressed
        player_one_handle_movement(keys_pressed, self.player_one)
        self.assertEqual(
            self.player_one.y, self.screen_height - self.player_one.height
        )  # Should stay at 0


if __name__ == "__main__":
    unittest.main()
