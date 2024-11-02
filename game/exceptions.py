class GameOver(Exception):
    """
    Exception raised when the player has no lives left.
    """
    pass


class EnemyDown(Exception):
    """
    Exception raised when the enemy has no lives left.
    """
    pass
