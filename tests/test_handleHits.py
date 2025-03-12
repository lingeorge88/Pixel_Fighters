import unittest
import pygame
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from game_logic import handle_hits


# Create a dummy sound manager object since we do not need sound to test the following game logic
class DummySoundManager:
    def play_hit_sound(self):
        pass


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.player_one_health = 10
        self.player_two_health = 10
        self.sound_manager = DummySoundManager()

    def test_player_one_hit(self):
        """
        Test the scenario where player one is hit.
        """
        # create a pygame event that correspond to the player being hit
        event = pygame.event.Event(pygame.USEREVENT + 1)
        # update the each player's health accordingly by passing in the hit event into the handle_hits function
        self.player_two_health, self.player_one_health = handle_hits(
            event, self.player_two_health, self.player_one_health, self.sound_manager
        )
        self.assertEqual(self.player_one_health, 9)
        self.assertEqual(self.player_two_health, 10)

    def test_player_two_hit(self):
        """
        Test the scenario where player two is hit.
        """
        event = pygame.event.Event(pygame.USEREVENT + 2)
        self.player_two_health, self.player_one_health = handle_hits(
            event, self.player_two_health, self.player_one_health, self.sound_manager
        )
        self.assertEqual(self.player_one_health, 10)
        self.assertEqual(self.player_two_health, 9)

    def test_both_players_hit(self):
        """
        Test the scenario where both players are hit at the same time.
        """
        # Create PLAYER_ONE_HIT and PLAYER_TWO_HIT events
        player_one_hit_event = pygame.event.Event(pygame.USEREVENT + 1)
        player_two_hit_event = pygame.event.Event(pygame.USEREVENT + 2)

        # Process PLAYER_ONE_HIT
        self.player_two_health, self.player_one_health = handle_hits(
            player_one_hit_event,
            self.player_two_health,
            self.player_one_health,
            self.sound_manager,
        )

        # Process PLAYER_TWO_HIT with updated health values
        self.player_two_health, self.player_one_health = handle_hits(
            player_two_hit_event,
            self.player_two_health,
            self.player_one_health,
            self.sound_manager,
        )

        # Assert that both players' health values are reduced
        self.assertEqual(self.player_one_health, 9)
        self.assertEqual(self.player_two_health, 9)

    def test_no_hit_event(self):
        """
        Test that health values remain unchanged for irrelevant events.
        """
        event = pygame.event.Event(
            pygame.USEREVENT + 3
        )  # This is an undefined user event so health values should not change for either player
        self.player_two_health, self.player_one_health = handle_hits(
            event, self.player_two_health, self.player_one_health, None
        )
        self.assertEqual(self.player_two_health, 10)
        self.assertEqual(self.player_one_health, 10)


if __name__ == "__main__":
    unittest.main()
