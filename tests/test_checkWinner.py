import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from game_logic import check_winner


class TestCheckWinner(unittest.TestCase):
    def setUp(self):
        """
        Set up player health and dummy data for testing.
        """
        self.player_one_health = 10
        self.player_two_health = 10
        self.player_one = None  # These can be None or mocked objects as they are unused
        self.player_two = None
        self.player_one_projectiles = []
        self.player_two_projectiles = []

    def test_no_winner(self):
        """
        Test that no winner is declared if both players have non-zero health.
        """
        result = check_winner(
            self.player_two_health,
            self.player_one_health,
            self.player_two,
            self.player_one,
            self.player_two_projectiles,
            self.player_one_projectiles,
        )
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
