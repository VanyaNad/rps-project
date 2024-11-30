from .models import Player, Enemy
from .settings import (
    MODE_HARD, HARD_MODE_MULTIPLIER, POINTS_FOR_FIGHT, POINTS_FOR_KILLING,
    WIN, LOSE, DRAW, ATTACK_PAIRS_OUTCOME, ENEMY_DEFEATED_MSG,
    QUIT_GAME_MSG, SCORE_SAVED_SUCCESS_MSG, LIVES_STATUS_MSG, PLAYER_WON_ROUND_MSG,
    PLAYER_LOST_ROUND_MSG, DRAW_MSG, POINTS_FOR_ENEMY_DEFEAT_MSG, PLAYER_CHOSE_MSG,
    ENEMY_CHOSE_MSG
)
from .exceptions import GameOver, EnemyDown, QuitGame, ScoreFileError
from .score import ScoreHandler


class Game:
    """Main game class managing player, enemy, and game loop"""

    def __init__(self, player: Player):
        self.player = player
        self.enemy = self.create_enemy()

    def create_enemy(self) -> Enemy:
        """Creates a new enemy with increased difficulty if in hard mode."""
        multiplier = HARD_MODE_MULTIPLIER if self.player.mode == MODE_HARD else 1
        # If the 'enemy' attribute exists, increment its level; otherwise, set it to 1
        level = self.enemy.level + 1 if hasattr(self, 'enemy') else 1
        # Ensure the level is at least 1
        level = max(1, level)
        return Enemy(level=level, difficulty_multiplier=multiplier)

    def play(self) -> None:
        """Starts the main game loop"""
        while True:
            try:
                self.display_lives()
                result = self.fight()
                self.handle_fight_result(result)
            except EnemyDown as e:
                print(e)
                self.player.add_score(POINTS_FOR_KILLING)
                print(POINTS_FOR_ENEMY_DEFEAT_MSG.format(POINTS_FOR_KILLING))
                print(ENEMY_DEFEATED_MSG)
                self.enemy = self.create_enemy()
            except GameOver as e:
                print(e)
                self.save_score()
                break
            except QuitGame as e:
                print(QUIT_GAME_MSG)
                self.save_score()
                break

    def fight(self) -> int:
        """Handles a single fight round between player and enemy"""
        try:
            player_attack = self.player.select_attack()
            enemy_attack = self.enemy.select_attack()
            print(f"\n{PLAYER_CHOSE_MSG.format(player_attack)}\n{ENEMY_CHOSE_MSG.format(enemy_attack)}\n")
            return ATTACK_PAIRS_OUTCOME[(player_attack, enemy_attack)]
        except QuitGame as e:
            raise QuitGame(e.message)

    def handle_fight_result(self, result: int) -> None:
        """Updates lives and score based on fight result"""
        if result == WIN:
            print(PLAYER_WON_ROUND_MSG)
            self.enemy.decrease_lives()
            self.player.add_score(POINTS_FOR_FIGHT)
        elif result == LOSE:
            print(PLAYER_LOST_ROUND_MSG)
            self.player.decrease_lives()
        else:
            print(DRAW_MSG)

    def save_score(self) -> None:
        """Saves the player's score at the end of the game."""
        try:
            score_handler = ScoreHandler()
            score_handler.save(self.player.name, self.player.mode, self.player.score)
            print(SCORE_SAVED_SUCCESS_MSG)
        except Exception as e:
            print(f"Error saving score: {e}")

    def display_lives(self) -> None:
        """Displays the current lives of both the player and the enemy"""
        print(LIVES_STATUS_MSG.format(self.player.lives, self.enemy.lives))
