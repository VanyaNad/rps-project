from .game import Game
from .models import Player
from .score import ScoreHandler
from .settings import (
    MAIN_MENU_TITLE, MENU_START_GAME_OPTION, MENU_SHOW_SCORES_OPTION,
    MENU_CLEAR_SCORES_OPTION, MENU_EXIT_OPTION, CHOOSE_OPTION_PROMPT,
    INVALID_MENU_OPTION_MSG, EXIT_GAME_MSG, ENTER_NAME_PROMPT, INVALID_NAME_MSG,
    DIFFICULTY_INPUT_PROMPT, INVALID_DIFFICULTY_MSG, CLEAR_SCORES_PROMPT,
    SCORES_CLEARED_MSG, SCORES_NOT_CLEARED_MSG, INVALID_CONFIRMATION_INPUT_MSG,
    MODES, NO_SCORES_MSG, YES, NO, START_GAMES, SHOW_SCORES, CLEAR_SCORES, QUIT
)


class GameHandler:
    """Handles the setup and flow of the game"""

    def start(self) -> None:
        """Starts the game loop, prompting the user for options"""
        while True:
            menu_options = self.display_menu()
            choice = input(CHOOSE_OPTION_PROMPT).strip().lower()

            if choice in menu_options:
                if choice == MENU_START_GAME_OPTION:
                    self.start_new_game()
                elif choice == MENU_SHOW_SCORES_OPTION:
                    self.show_scores()
                elif choice == MENU_CLEAR_SCORES_OPTION:
                    self.clear_scores()
                elif choice == MENU_EXIT_OPTION:
                    print(EXIT_GAME_MSG)
                    break
            else:
                print(INVALID_MENU_OPTION_MSG)

    def display_menu(self) -> list[str]:
        """Displays the main menu, showing Show Scores and Clear Scores options only if scores exist"""
        menu_options = []

        print(f"\n{MAIN_MENU_TITLE}")

        # Display Start Game Option
        menu_options.append(MENU_START_GAME_OPTION)
        print(f"({MENU_START_GAME_OPTION}) {START_GAMES}")

        # Display Show Scores and Clear Scores options if scores exist
        if self.scores_exist():
            menu_options.append(MENU_SHOW_SCORES_OPTION)
            print(f"({MENU_SHOW_SCORES_OPTION}) {SHOW_SCORES}")

            menu_options.append(MENU_CLEAR_SCORES_OPTION)
            print(f"({MENU_CLEAR_SCORES_OPTION}) {CLEAR_SCORES}")

        # Display Quit Option
        menu_options.append(MENU_EXIT_OPTION)
        print(f"({MENU_EXIT_OPTION}) {QUIT}")

        return menu_options

    def start_new_game(self) -> None:
        """Initializes and starts a new game"""
        player_name = self.get_valid_name()
        difficulty = self.select_difficulty()
        player = Player(name=player_name, mode=difficulty)
        game = Game(player)
        game.play()

    def get_valid_name(self) -> str:
        """Asks the user for a valid name, ensuring that it only contains alphabetic characters"""
        while True:
            name = input(ENTER_NAME_PROMPT).strip()
            if self.validate_name(name):
                return name
            else:
                print(INVALID_NAME_MSG)

    def select_difficulty(self) -> str:
        """Ask for difficulty level"""
        while True:
            mode_choice = input(DIFFICULTY_INPUT_PROMPT).strip()
            if self.validate_difficulty_choice(mode_choice):
                return MODES[mode_choice]
            else:
                print(INVALID_DIFFICULTY_MSG)

    def show_scores(self) -> None:
        """Displays saved scores"""
        score_handler = ScoreHandler()
        if self.scores_exist():
            score_handler.display()
        else:
            print(NO_SCORES_MSG)

    @staticmethod
    def clear_scores() -> None:
        """Clears all scores if needed"""
        while True:
            confirmation = input(CLEAR_SCORES_PROMPT).strip().lower()
            if confirmation == YES:
                score_handler = ScoreHandler()
                score_handler.clear()
                print(SCORES_CLEARED_MSG)
                break
            elif confirmation == NO:
                print(SCORES_NOT_CLEARED_MSG)
                break
            else:
                print(INVALID_CONFIRMATION_INPUT_MSG)

    @staticmethod
    def scores_exist() -> bool:
        """Checks if there are existing scores"""
        score_handler = ScoreHandler()
        return len(score_handler.records) > 0

    @staticmethod
    def validate_name(name: str) -> bool:
        """Validates that the name contains only alphabetic characters"""
        return name.isalpha()

    @staticmethod
    def validate_difficulty_choice(choice: str) -> bool:
        """Validates that the difficulty choice is either 1 or 2"""
        return choice in MODES
