# game/models.py - Player and Enemy models
from game.settings import PLAYER_LIVES, ALLOWED_ATTACKS
from game.exceptions import GameOver, EnemyDown
import random


class Player:
    def __init__(self, name: str) -> None:
        """
        Initialize the player with a name, lives, and score.
        """
        self.name = name
        self.lives = PLAYER_LIVES
        self.score = 0

    def select_attack(self) -> str:
        """
        Prompt the player to select an attack.
        """
        while True:
            attack = input(f"Select your attack ({', '.join(ALLOWED_ATTACKS.keys())}): ")
            if attack in ALLOWED_ATTACKS:
                return ALLOWED_ATTACKS[attack]
            print("Invalid choice. Please try again.")

    def decrease_lives(self) -> None:
        """
        Decrease player's lives by 1. Raise GameOver exception if no lives remain.
        """
        self.lives -= 1
        if self.lives <= 0:
            raise GameOver(f"{self.name} has no lives left!")

    def add_score(self, points: int) -> None:
        """
        Add points to the player's score.
        """
        self.score += points


class Enemy:
    def __init__(self, level: int) -> None:
        """
        Initialize the enemy with a level and corresponding lives.
        """
        self.level = level
        self.lives = level

    def select_attack(self) -> str:
        """
        Randomly select an attack for the enemy.
        """
        return random.choice(list(ALLOWED_ATTACKS.values()))

    def decrease_lives(self) -> None:
        """
        Decrease enemy's lives by 1. Raise EnemyDown exception if no lives remain.
        """
        self.lives -= 1
        if self.lives <= 0:
            raise EnemyDown("Enemy has been defeated!")



