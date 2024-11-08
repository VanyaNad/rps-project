import random
from .settings import PLAYER_LIVES, ENEMY_BASE_LIVES, ALLOWED_ATTACKS, PLAYER_ATTACK_INPUT_PROMPT, \
    INVALID_ATTACK_CHOICE_MSG, ENEMY_DOWN_EXCEPTION_MSG
from .exceptions import GameOver, EnemyDown, QuitGame


class Player:
    """Represents the player in the game"""

    def __init__(self, name: str, mode: str) -> None:
        """
        Init the player with a name, lives, score, and game mode

        Args:
            name (str): The player's name.
            mode (str): The game mode (Normal or Hard).
        """
        self.name: str = name
        self.lives: int = PLAYER_LIVES
        self.score: int = 0
        self.mode: str = mode

    @staticmethod
    def select_attack() -> str:
        """Ask player to choose an attack

        Returns:
          str: The chosen attack option.

        Raises:
            QuitGame: If the player chooses to quit the game
        """
        while True:
            attack_choice: str = input(PLAYER_ATTACK_INPUT_PROMPT).strip().lower()
            if attack_choice in ALLOWED_ATTACKS:
                return ALLOWED_ATTACKS[attack_choice]
            elif attack_choice == 'q':
                raise QuitGame("Player chose to quit the game.")
            else:
                print(INVALID_ATTACK_CHOICE_MSG)

    def decrease_lives(self) -> None:
        """Decreases player's lives by 1 and checks if the player is out of lives

        Raises
            GameOver: If the player's lives reach zero
        """
        self.lives -= 1
        if self.lives <= 0:
            raise GameOver("Game Over! Player has lost all lives.")

    def add_score(self, points: int) -> None:
        """Add points to the player's score

        Args:
            points (int): The number of points to add
        """
        self.score += points


class Enemy:
    """Represents the enemy in the game."""

    def __init__(self, level: int, difficulty_multiplier: int = 1) -> None:
        """
        Init the enemy with level and calculates lives based on difficulty

        Args:
            level (int): The level of the enemy
            difficulty_multiplier (int): Multiplier for difficulty (used for number of lives)
        """
        self.level: int = level
        self.lives: int = ENEMY_BASE_LIVES * difficulty_multiplier * level

    @staticmethod
    def select_attack() -> str:
        """Randomly selects an attack for the enemy

        Returns:
            str: The chosen attack option
        """
        return random.choice(list(ALLOWED_ATTACKS.values()))

    def decrease_lives(self) -> None:
        """Decreases enemy's lives by 1 and checks if the enemy is out of lives

        Raises:
            EnemyDown: If the enemy's lives reach zero
        """
        self.lives -= 1
        if self.lives <= 0:
            raise EnemyDown(ENEMY_DOWN_EXCEPTION_MSG)
