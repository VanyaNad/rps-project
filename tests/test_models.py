import unittest
from game.models import Player, Enemy
from game.exceptions import GameOver, EnemyDown


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(name="Alice", mode="Normal")

    def test_initialization(self):
        self.assertEqual(self.player.name, "Alice")
        self.assertEqual(self.player.lives, 3)
        self.assertEqual(self.player.score, 0)

    def test_negative_score(self):
        self.player.add_score(-50)
        self.assertEqual(self.player.score, -50)

    def test_high_lives(self):
        self.player.lives = 1000
        self.player.decrease_lives()
        self.assertEqual(self.player.lives, 999)


    def test_life_reduction(self):
        for lives in range(1, 11):
            self.player.lives = lives
            if lives > 1:
                self.player.decrease_lives()
                self.assertEqual(self.player.lives, lives - 1)
            else:
                with self.assertRaises(GameOver):
                    self.player.decrease_lives()


class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.enemy = Enemy(level=1)

    def test_initialization(self):
        self.assertEqual(self.enemy.level, 1)
        self.assertGreater(self.enemy.lives, 0)

    def test_life_reduction(self):
        for lives in range(1, 11):
            self.enemy.lives = lives
            if lives > 1:
                self.enemy.decrease_lives()
                self.assertEqual(self.enemy.lives, lives - 1)
            else:
                with self.assertRaises(EnemyDown):
                    self.enemy.decrease_lives()


class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.enemy = Enemy(level=1)

    def test_high_enemy_lives(self):
        self.enemy.lives = 500
        self.enemy.decrease_lives()
        self.assertEqual(self.enemy.lives, 499)


if __name__ == "__main__":
    unittest.main()
