from .settings import (
    SCORE_FILE, MAX_RECORDS_NUMBER, SCORES_WRITE_ERROR_MSG,
    FILE_NOT_FOUND_MSG, SCORES_WRITTEN_SUCCESS_MSG, NO_SCORES_FOUND_MSG,
    SKIPPING_INVALID_RECORD_MSG, TOP_SCORES_TITLE_MSG
)
from .exceptions import ScoreFileError
from typing import List


class PlayerRecord:
    """Represents a single player's score record"""

    def __init__(self, name: str, mode: str, score: int):
        self.name = name
        self.mode = mode
        self.score = int(score)

    def __str__(self) -> str:
        return f"{self.name}\t{self.mode}\t{self.score}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PlayerRecord):
            return NotImplemented
        return self.name == other.name and self.mode == other.mode

    def __lt__(self, other: "PlayerRecord") -> bool:
        return self.score < other.score


class ScoreHandler:
    """Manages score reading, saving, displaying, and clearing"""

    def __init__(self):
        self.records: List[PlayerRecord] = self.read_scores()

    @staticmethod
    def read_scores() -> List[PlayerRecord]:
        """Reads scores from a file"""
        records = []
        try:
            with open(SCORE_FILE, 'r') as file:
                for line in file:
                    try:
                        name, mode, score = line.strip().split('\t')
                        records.append(PlayerRecord(name, mode, int(score)))
                    except ValueError:
                        print(SKIPPING_INVALID_RECORD_MSG.format(line.strip()))
        except FileNotFoundError:
            print(FILE_NOT_FOUND_MSG.format(SCORE_FILE))
        return records

    def save(self, player, mode: str) -> None:
        """Saves a player's score to the file, updating existing records if needed"""
        new_record = PlayerRecord(player.name, mode, player.score)

        updated = False
        for record in self.records:
            if record == new_record:
                if new_record.score > record.score:
                    record.score = new_record.score
                updated = True
                break

        if not updated:
            self.records.append(new_record)

        self.records = sorted(self.records, key=lambda r: r.score, reverse=True)[:MAX_RECORDS_NUMBER]
        self.write_scores()

    def write_scores(self) -> None:
        """Writes the current records to the score file."""
        try:
            with open(SCORE_FILE, 'w') as file:
                for record in self.records:
                    file.write(str(record) + "\n")
            print(SCORES_WRITTEN_SUCCESS_MSG.format(SCORE_FILE))
        except IOError as e:
            raise ScoreFileError(SCORES_WRITE_ERROR_MSG.format(e))

    def display(self) -> None:
        """Displays the top scores"""
        print(f"\n{TOP_SCORES_TITLE_MSG}")
        if not self.records:
            print(NO_SCORES_FOUND_MSG)
        else:
            for record in self.records:
                print(record)
        print("\n")

    def clear(self) -> None:
        """Clears all the records from the score file"""
        try:
            with open(SCORE_FILE, 'w') as file:
                file.write('')
            self.records = []
        except IOError as e:
            raise ScoreFileError(SCORES_WRITE_ERROR_MSG.format(e))
