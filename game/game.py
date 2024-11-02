from game.models import Player, Enemy
from game.settings import ATTACK_PAIRS_OUTCOME, WIN, LOSE, POINTS_FOR_FIGHT, POINTS_FOR_KILLING
from game.exceptions import GameOver, EnemyDown
from game.score import ScoreHandler


class Game:
    def __init__(self, player: Player, mode: str) -> None:
        """
        Initialize the game with a player, difficulty mode, and the first enemy.
        """
        self.player = player
        self.mode = mode
        self.enemy = self.create_enemy(1)

    def create_enemy(self, level: int) -> Enemy:
        """
        Create a new enemy with the given level.
        """
        return Enemy(level)

    def play(self) -> None:
        """
        Start the game loop where the player fights enemies until game over.
        """
        while True:
            try:
                self.fight()
            except GameOver:
                print("Game Over!")
                self.save_score()
                break
            except EnemyDown:
                print("Enemy defeated!")
                self.player.add_score(POINTS_FOR_KILLING)
                self.enemy = self.create_enemy(self.enemy.level + 1)

    def fight(self) -> None:
        """
        Handle a fight between the player and the enemy.
        """
        player_attack = self.player.select_attack()
        enemy_attack = self.enemy.select_attack()
        print(f"Player chose {player_attack}, Enemy chose {enemy_attack}")
        result = ATTACK_PAIRS_OUTCOME[(player_attack, enemy_attack)]
        self.handle_fight_result(result)

    def handle_fight_result(self, result: int) -> None:
        """
        Handle the result of a fight round.
        """
        if result == WIN:
            print("You won this round!")
            self.enemy.decrease_lives()
            self.player.add_score(POINTS_FOR_FIGHT)
        elif result == LOSE:
            print("You lost this round!")
            self.player.decrease_lives()
        else:
            print("It's a draw!")

    def save_score(self) -> None:
        """
        Save the player's score using the ScoreHandler.
        """
        score_handler = ScoreHandler()
        score_handler.add_record(self.player)
        score_handler.save()

