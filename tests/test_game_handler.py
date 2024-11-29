import unittest
from unittest.mock import patch
from game.game_handler import GameHandler


class TestGameHandler(unittest.TestCase):
    def setUp(self):
        self.handler = GameHandler()

    def test_menu_display_with_scores(self):
        with patch("game.game_handler.GameHandler.scores_exist", return_value=True):
            menu = self.handler.display_menu()
            self.assertIn("1", menu)
            self.assertIn("2", menu)
            self.assertIn("3", menu)
            self.assertIn("q", menu)


    def test_difficulty_selection_retries(self):
        with patch("builtins.input", side_effect=["abc", "x", "1"]):
            self.assertEqual(self.handler.select_difficulty(), "Normal")

    def test_menu_display_without_scores(self):
        with patch("game.game_handler.GameHandler.scores_exist", return_value=False):
            menu = self.handler.display_menu()
            self.assertIn("1", menu)
            self.assertIn("q", menu)

    def test_valid_player_name(self):
        valid_names = ["John", "Alice", "Bob", "Kate", "Eve"]
        for name in valid_names:
            with patch("builtins.input", return_value=name):
                self.assertEqual(self.handler.get_valid_name(), name)

    def test_invalid_player_name(self):
        invalid_names = ["", "123", "!@#"]
        for name in invalid_names:
            with patch("builtins.input", side_effect=[name, "John"]):
                self.assertEqual(self.handler.get_valid_name(), "John")

    def test_difficulty_selection(self):
        valid_inputs = [("1", "Normal"), ("2", "Hard")]
        for user_input, difficulty in valid_inputs:
            with patch("builtins.input", return_value=user_input):
                self.assertEqual(self.handler.select_difficulty(), difficulty)

    def test_invalid_difficulty_selection(self):
        invalid_inputs = ["3", "x", "-1", ""]
        for invalid_input in invalid_inputs:
            with patch("builtins.input", side_effect=[invalid_input, "1"]):
                self.assertEqual(self.handler.select_difficulty(), "Normal")


if __name__ == "__main__":
    unittest.main()
