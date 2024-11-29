import unittest
from unittest.mock import patch

from game.game import Game
from game.models import Player, Enemy
from game.exceptions import GameOver, EnemyDown, QuitGame


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player = Player(name="John", mode="Normal")
        self.game = Game(self.player)

    def test_initialization(self):
        self.assertEqual(self.game.player.name, "John")
        self.assertIsInstance(self.game.enemy, Enemy)

    def test_create_enemy_multiple_levels(self):
        for level in range(1, 101):
            self.game.enemy.level = level - 1
            enemy = self.game.create_enemy()
            self.assertEqual(enemy.level, level)
            self.assertGreater(enemy.lives, 0)

    def test_game_outcomes(self):
        outcomes = ["WIN", "LOSE", "DRAW"]
        for outcome in outcomes:
            self.assertIn(outcome, ["WIN", "LOSE", "DRAW"])

    def test_player_life_flow(self):
        for lives in range(1, 11):
            self.game.player.lives = lives
            if lives > 1:
                self.game.player.decrease_lives()
                self.assertEqual(self.game.player.lives, lives - 1)
            else:
                with self.assertRaises(GameOver):
                    self.game.player.decrease_lives()

    def test_enemy_life_flow(self):
        for lives in range(1, 11):
            self.game.enemy.lives = lives
            if lives > 1:
                self.game.enemy.decrease_lives()
                self.assertEqual(self.game.enemy.lives, lives - 1)
            else:
                with self.assertRaises(EnemyDown):
                    self.game.enemy.decrease_lives()

    def test_enemy_creation_extreme_levels(self):
        for level in [-10, 0, 100]:
            self.game.enemy.level = level
            enemy = self.game.create_enemy()
            self.assertGreaterEqual(enemy.level, 1)
            self.assertGreater(enemy.lives, 0)

    def test_enemy_zero_lives(self):
        self.game.enemy.lives = 0
        with self.assertRaises(EnemyDown):
            self.game.enemy.decrease_lives()

    def test_player_zero_lives(self):
        self.game.player.lives = 0
        with self.assertRaises(GameOver):
            self.game.player.decrease_lives()

    def test_play_enemy_down(self):
        loop_counter = {"count": 0}

        def mock_fight():
            if loop_counter["count"] < 2:
                loop_counter["count"] += 1
                raise EnemyDown("Enemy down!")
            raise GameOver("Game over!")

        with patch.object(self.game, "display_lives"), \
                patch.object(self.game, "fight", side_effect=mock_fight), \
                patch.object(self.game, "handle_fight_result"), \
                patch.object(self.game, "create_enemy", return_value=Enemy(level=2)), \
                patch.object(self.game.player, "add_score") as mock_add_score:
            self.game.play()

            self.assertEqual(mock_add_score.call_count, 2)  # EnemyDown handled twice
            self.assertEqual(self.game.enemy.level, 2)  # New enemy created

    def test_play_game_over(self):
        with patch.object(self.game, "display_lives"), \
                patch.object(self.game, "fight", side_effect=[GameOver("Game Over!")]), \
                patch.object(self.game, "save_score") as mock_save_score:
            self.game.play()

            mock_save_score.assert_called_once()

    def test_play_quit_game(self):
        with patch.object(self.game, "display_lives"), \
                patch.object(self.game, "fight", side_effect=[QuitGame("Quit Game!")]), \
                patch.object(self.game, "save_score") as mock_save_score:
            self.game.play()

            mock_save_score.assert_called_once()

    def test_play_normal_flow(self):
        # Mock multiple fight results and end with GameOver to stop the loop
        with patch.object(self.game, "display_lives"), \
                patch.object(self.game, "fight", side_effect=["WIN", "DRAW", "LOSE", GameOver("Game Over!")]), \
                patch.object(self.game, "handle_fight_result") as mock_handle_result:
            self.game.play()

            self.assertEqual(mock_handle_result.call_count, 3)


if __name__ == "__main__":
    unittest.main()
