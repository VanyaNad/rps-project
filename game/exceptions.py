from .settings import (
    GAME_OVER_EXCEPTION_MSG, ENEMY_DOWN_EXCEPTION_MSG, INVALID_ATTACK_EXCEPTION_MSG,
    QUIT_GAME_EXCEPTION_MSG, INVALID_MENU_OPTION_MSG, SCORE_FILE_ERROR_MSG
)


class GameOver(Exception):
    """Raised when the player's lives reach zero"""
    def __init__(self, message=GAME_OVER_EXCEPTION_MSG):
        self.message = message
        super().__init__(self.message)


class EnemyDown(Exception):
    """Raised when the enemy's lives reach zero"""
    def __init__(self, message=ENEMY_DOWN_EXCEPTION_MSG):
        self.message = message
        super().__init__(self.message)


class InvalidAttack(Exception):
    """Raised when invalid attack"""
    def __init__(self, message=INVALID_ATTACK_EXCEPTION_MSG):
        self.message = message
        super().__init__(self.message)


class QuitGame(Exception):
    """Raised when the player decides to quit the game"""
    def __init__(self, message=QUIT_GAME_EXCEPTION_MSG):
        self.message = message
        super().__init__(self.message)


class InvalidMenuOption(Exception):
    """Raised when an invalid menu option is chosen"""
    def __init__(self, message=INVALID_MENU_OPTION_MSG):
        self.message = message
        super().__init__(self.message)


class ScoreFileError(Exception):
    """Raised when there is an error in handling the score file"""
    def __init__(self, message=SCORE_FILE_ERROR_MSG):
        self.message = message
        super().__init__(self.message)
