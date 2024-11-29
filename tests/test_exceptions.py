import unittest
from game.exceptions import GameOver, EnemyDown, InvalidAttack, QuitGame, InvalidMenuOption, ScoreFileError
from game.settings import (GAME_OVER_EXCEPTION_MSG, ENEMY_DOWN_EXCEPTION_MSG, INVALID_ATTACK_EXCEPTION_MSG,
                           QUIT_GAME_EXCEPTION_MSG, INVALID_MENU_OPTION_MSG, SCORE_FILE_ERROR_MSG)


class TestExceptions(unittest.TestCase):

    def assert_exception(self, exception_cls, exception_msg):
        with self.assertRaises(exception_cls) as e:
            raise exception_cls()
        self.assertEqual(str(e.exception), exception_msg)

    def test_game_over(self):
        self.assert_exception(GameOver, GAME_OVER_EXCEPTION_MSG)

    def test_enemy_down(self):
        self.assert_exception(EnemyDown, ENEMY_DOWN_EXCEPTION_MSG)

    def test_invalid_attack(self):
        self.assert_exception(InvalidAttack, INVALID_ATTACK_EXCEPTION_MSG)

    def test_quit_game(self):
        self.assert_exception(QuitGame, QUIT_GAME_EXCEPTION_MSG)

    def test_invalid_menu_option(self):
        self.assert_exception(InvalidMenuOption, INVALID_MENU_OPTION_MSG)

    def test_score_file_error(self):
        self.assert_exception(ScoreFileError, SCORE_FILE_ERROR_MSG)
