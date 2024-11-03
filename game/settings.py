# Modes
MODE_NORMAL = 'Normal'
MODE_HARD = 'Hard'
MODES = {'1': MODE_NORMAL, '2': MODE_HARD}

# Player Settings
PLAYER_LIVES = 3
ENEMY_BASE_LIVES = 2
HARD_MODE_MULTIPLIER = 2

# Points
POINTS_FOR_FIGHT = 1
POINTS_FOR_KILLING = 5
MAX_RECORDS_NUMBER = 5

# File Paths
SCORE_FILE = 'scores.txt'

# Attack Types
PAPER = 'Paper'
STONE = 'Stone'
SCISSORS = 'Scissors'

# Attack Outcomes
WIN = 1
DRAW = 0
LOSE = -1

# Attack Options
ALLOWED_ATTACKS = {'1': PAPER, '2': STONE, '3': SCISSORS}

# Attack Pair Outcomes
ATTACK_PAIRS_OUTCOME = {
    (PAPER, PAPER): DRAW,
    (PAPER, STONE): WIN,
    (PAPER, SCISSORS): LOSE,
    (STONE, PAPER): LOSE,
    (STONE, STONE): DRAW,
    (STONE, SCISSORS): WIN,
    (SCISSORS, PAPER): WIN,
    (SCISSORS, STONE): LOSE,
    (SCISSORS, SCISSORS): DRAW
}

# Score Messages
FILE_NOT_FOUND_MSG = "No score file found. Creating a new one at: {}"
SCORES_WRITE_ERROR_MSG = "Error saving scores to the file: {}"
SCORES_WRITTEN_SUCCESS_MSG = "Scores have been successfully written to {}."
NO_SCORES_FOUND_MSG = "No records found."
SKIPPING_INVALID_RECORD_MSG = "Skipping invalid record: {}"
TOP_SCORES_TITLE_MSG = "--- Top Scores ---"

# General Game Messages
ENEMY = 'enemy'
PLAYER_CHOSE_MSG = "Player chose: {}"
ENEMY_CHOSE_MSG = "Enemy chose: {}"
GAME_OVER_MSG = "Game Over! Player has lost all lives."
ENEMY_DEFEATED_MSG = "Enemy defeated! A stronger enemy appears..."
QUIT_GAME_MSG = "Thank you for playing! See you next time!"
SCORE_SAVED_SUCCESS_MSG = "Your score has been saved successfully."
POINTS_FOR_ENEMY_DEFEAT_MSG = "You received {} points for defeating the enemy."
PLAYER_WON_ROUND_MSG = "You won the round!"
PLAYER_LOST_ROUND_MSG = "You lost the round."
DRAW_MSG = "It's a draw!"
LIVES_STATUS_MSG = "\n--- Current Lives ---\nPlayer Lives: {}\nEnemy Lives: {}\n----------------------\n"

# Player Messages
PLAYER_LOST_LIVES_MSG = "Game Over! Player has lost all lives."
PLAYER_QUIT_GAME_MSG = "Player chose to quit the game."
PLAYER_ATTACK_INPUT_PROMPT = "Choose your attack: (1) Paper, (2) Stone, (3) Scissors, (q) Quit: "
INVALID_ATTACK_CHOICE_MSG = "Invalid attack choice. Please enter 1, 2, or 3."

# Menu Options and Messages
MAIN_MENU_TITLE = "--- Main Menu ---"
MENU_START_GAME_OPTION = "1"
MENU_SHOW_SCORES_OPTION = "2"
MENU_CLEAR_SCORES_OPTION = "3"
MENU_EXIT_OPTION = "q"

CHOOSE_OPTION_PROMPT = "Choose an option: "
INVALID_MENU_OPTION_MSG = "Invalid choice. Please enter a valid option from the menu."

EXIT_GAME_MSG = "Exiting... Goodbye!"

ENTER_NAME_PROMPT = "Enter your name: "
INVALID_NAME_MSG = "Invalid name. Please enter a name using only alphabetic characters."

DIFFICULTY_INPUT_PROMPT = "Choose difficulty: (1) Normal, (2) Hard: "
INVALID_DIFFICULTY_MSG = "Invalid choice. Please enter 1 for Normal or 2 for Hard."

CLEAR_SCORES_PROMPT = "Are you sure you want to clear all scores? (y/n): "
SCORES_CLEARED_MSG = "All scores have been cleared successfully."
SCORES_NOT_CLEARED_MSG = "Scores not cleared."
INVALID_CONFIRMATION_INPUT_MSG = "Invalid input. Please enter 'y' for yes or 'n' for no."

NO_SCORES_MSG = "--- Top Scores ---\nNo records found.\n"

# Confirmation Inputs
YES = 'y'
NO = 'n'

# Exception Messages
GAME_OVER_EXCEPTION_MSG = "Game Over! Player has lost all lives."
ENEMY_DOWN_EXCEPTION_MSG = "Enemy defeated."
INVALID_ATTACK_EXCEPTION_MSG = "Invalid attack choice."
QUIT_GAME_EXCEPTION_MSG = "The player has chosen to quit the game."
INVALID_MENU_OPTION_EXCEPTION_MSG = "Invalid menu option selected. Please choose 1, 2, or 3."
SCORE_FILE_ERROR_MSG = "There was an issue with the score file."