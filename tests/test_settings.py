import unittest
from game.settings import (
    PLAYER_LIVES,
    ENEMY_BASE_LIVES,
    ALLOWED_ATTACKS,
    PLAYER_ATTACK_INPUT_PROMPT,
    INVALID_ATTACK_CHOICE_MSG,
    ENEMY_DOWN_EXCEPTION_MSG,
    GAME_OVER_EXCEPTION_MSG,
    MODES,
    HARD_MODE_MULTIPLIER,
    ZERO,
    ONE,
    TWO
)


class TestSettings(unittest.TestCase):

    def test_player_lives(self):
        self.assertIsInstance(PLAYER_LIVES, int)
        self.assertGreater(PLAYER_LIVES, ZERO)

    def test_enemy_base_lives(self):
        self.assertIsInstance(ENEMY_BASE_LIVES, int)
        self.assertGreater(ENEMY_BASE_LIVES, ZERO)

    def test_allowed_attacks(self):
        self.assertIsInstance(ALLOWED_ATTACKS, dict)
        self.assertTrue(len(ALLOWED_ATTACKS) > ZERO)
        for key, value in ALLOWED_ATTACKS.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, str)

    def test_player_attack_input_prompt(self):
        self.assertIsInstance(PLAYER_ATTACK_INPUT_PROMPT, str)

    def test_invalid_attack_choice_msg(self):
        self.assertIsInstance(INVALID_ATTACK_CHOICE_MSG, str)

    def test_enemy_down_exception_msg(self):
        self.assertIsInstance(ENEMY_DOWN_EXCEPTION_MSG, str)

    def test_game_over_exception_msg(self):
        self.assertIsInstance(GAME_OVER_EXCEPTION_MSG, str)

    def test_modes(self):
        self.assertIsInstance(MODES, dict)
        self.assertIn(f"{ONE}", MODES)
        self.assertIn(f"{TWO}", MODES)

    def test_hard_mode_multiplier(self):
        self.assertIsInstance(HARD_MODE_MULTIPLIER, int)
        self.assertGreaterEqual(HARD_MODE_MULTIPLIER, ONE)
