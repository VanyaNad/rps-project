from game.settings import MODES
from game.models import Player
from game.score import ScoreHandler
from game.game import Game


def main() -> None:
    """
    Main function to handle the game menu.
    Allows user to choose between starting the game, viewing scores, or exiting.
    """
    while True:
        print("\n--- Rock-Paper-Scissors Game Menu ---")
        print("1. Start Game")
        print("2. View Scores")
        print("3. Exit")
        choice = input("Choose an option (1, 2, 3): ")

        if choice == '1':
            play_game()
        elif choice == '2':
            show_scores()
        elif choice == '3':
            exit_game()
        else:
            print("Invalid choice. Please try again.")


def play_game() -> None:
    """
    Function to start the game by creating a player and running the game.
    """
    player_name = input("Enter your name: ")
    print("Select difficulty level:")
    for key, value in MODES.items():
        print(f"{key}: {value}")
    mode_choice = input("Choose a mode (1 or 2): ")
    mode = MODES.get(mode_choice, MODES['1'])

    player = Player(player_name)
    game = Game(player, mode)
    game.play()


def show_scores() -> None:
    """
    Function to display the high scores.
    """
    score_handler = ScoreHandler()
    score_handler.display()


def exit_game() -> None:
    """
    Function to exit the game.
    """
    print("Goodbye!")
    exit()


if __name__ == "__main__":
    main()
    