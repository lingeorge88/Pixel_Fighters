import unittest
import pygame
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from movement_logic import player_two_handle_movement
from settings import VEL, WIDTH, HEIGHT, BORDER


class MockKeys:
    """
    Mock pygame key presses for testing.
    """

    def __init__(self, keys):
        self.keys = keys

    def __getitem__(self, key):
        return self.keys.get(key, False)


class TestPlayerTwoMovementLogic(unittest.TestCase):
    def setUp(self):
        """
        Set up game screen dimensions, initial player positions, and velocities.
        """
        self.screen_width = WIDTH  # Width of the game screen is 900
        self.screen_height = HEIGHT  # Height of the game screen is 500 pixels
        self.border = BORDER  # Border object from settings in the middle of the screen
        self.player_two = pygame.Rect(750, 350, 50, 50)  # Player Two's rectangle
        self.velocity = VEL  # Player moves at 5 pixels per key press

    def test_player_two_move_left(self):
        """
        Test that Player Two moves left within screen boundaries.
        """
        keys_pressed = MockKeys({pygame.K_LEFT: True})  # Left arrow pressed
        player_two_handle_movement(keys_pressed, self.player_two)
        self.assertEqual(self.player_two.x, 745)  # 700 - 5

    def test_player_two_move_right(self):
        """
        Test that Player Two moves right within screen boundaries.
        """
        keys_pressed = MockKeys({pygame.K_RIGHT: True})  # Right arrow pressed
        player_two_handle_movement(keys_pressed, self.player_two)
        self.assertEqual(self.player_two.x, 755)  # 700 + 5

    def test_player_two_move_left_boundary(self):
        """
        Test that Player Two does not move beyond the left boundary defined by BORDER.x + BORDER.width.
        """
        self.player_two.x = (
            self.border.x + self.border.width
        )  # At the right edge of the border
        keys_pressed = MockKeys({pygame.K_LEFT: True})  # Left arrow pressed
        player_two_handle_movement(keys_pressed, self.player_two)
        self.assertEqual(
            self.player_two.x, self.border.x + self.border.width
        )  # Should stay at the border

    def test_player_two_move_right_boundary(self):
        """
        Test that Player Two does not move off the right edge of the screen.
        """
        self.player_two.x = (
            self.screen_width - self.player_two.width
        )  # At the right edge of the screen
        keys_pressed = MockKeys({pygame.K_RIGHT: True})  # Right arrow pressed
        player_two_handle_movement(keys_pressed, self.player_two)
        self.assertEqual(self.player_two.x, self.screen_width - self.player_two.width)

    def test_player_two_move_up(self):
        """
        Test that Player Two moves up within screen boundaries.
        """
        keys_pressed = MockKeys({pygame.K_UP: True})  # Up arrow pressed
        player_two_handle_movement(keys_pressed, self.player_two)
        self.assertEqual(self.player_two.y, 345)  # 350 - 5

    def test_player_two_move_up_boundary(self):
        """
        Test that Player Two does not move off the top boundary.
        """
        self.player_two.y = 0  # Already at the top boundary
        keys_pressed = MockKeys({pygame.K_UP: True})  # Up arrow pressed
        player_two_handle_movement(keys_pressed, self.player_two)
        self.assertEqual(self.player_two.y, 0)  # Should stay at 0

    def test_player_two_move_down(self):
        """
        Test that Player Two moves down within screen boundaries.
        """
        keys_pressed = MockKeys({pygame.K_DOWN: True})  # Down arrow pressed
        player_two_handle_movement(keys_pressed, self.player_two)
        self.assertEqual(self.player_two.y, 355)  # 350 + 5

    def test_player_two_move_down_boundary(self):
        """
        Test that Player Two does not move off the bottom boundary.
        """
        self.player_two.y = (
            self.screen_height - self.player_two.height
        )  # At bottom edge
        keys_pressed = MockKeys({pygame.K_DOWN: True})  # Down arrow pressed
        player_two_handle_movement(keys_pressed, self.player_two)
        self.assertEqual(self.player_two.y, self.screen_height - self.player_two.height)


if __name__ == "__main__":
    unittest.main()
