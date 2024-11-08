import unittest
from game.models import Player
from game.models import Player
from game.settings import PLAYER_LIVES, ZERO


class TestModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.name = "TestPlayer"
        cls.mode = "Normal"
        cls.player = Player(name=cls.name, mode=cls.mode)

    def test_player_init_name(self):
        self.assertIsInstance(self.player.name, str)
        self.assertEqual(self.player.name, self.name)

    def test_player_init_mode(self):
        self.assertIsInstance(self.player.name, str)
        self.assertEqual(self.player.mode, self.mode)

    def test_player_init_score(self):
        self.assertIsInstance(self.player.score, int)
        self.assertTrue(self.player.score >= 0)

    def test_player_init_lives(self):
        self.assertIsInstance(self.player.score, int)
        self.assertTrue(self.player.lives == PLAYER_LIVES)
