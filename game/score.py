from game.settings import SCORE_FILE, MAX_RECORDS_NUMBER


class PlayerRecord:
    def __init__(self, name: str, mode: str, score: int) -> None:
        self.name = name
        self.mode = mode
        self.score = score

    def __gt__(self, other: 'PlayerRecord') -> bool:
        return self.score > other.score

    def __str__(self) -> str:
        return f"{self.name}\t{self.mode}\t{self.score}"


class GameRecord:
    def __init__(self) -> None:
        self.records = []

    def add_record(self, record: PlayerRecord) -> None:
        for existing_record in self.records:
            if existing_record.name == record.name and existing_record.mode == record.mode:
                existing_record.score = max(existing_record.score, record.score)
                return
        self.records.append(record)

    def prepare_records(self) -> None:
        self.records.sort(reverse=True)
        self.records = self.records[:MAX_RECORDS_NUMBER]


class ScoreHandler:
    def __init__(self) -> None:
        self.file_name = SCORE_FILE
        self.game_record = GameRecord()
        self.read()

    def read(self) -> None:
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    name, mode, score = line.strip().split('\t')
                    self.game_record.add_record(PlayerRecord(name, mode, int(score)))
        except FileNotFoundError:
            pass

    def save(self) -> None:
        self.game_record.prepare_records()
        with open(self.file_name, 'w') as file:
            for record in self.game_record.records:
                file.write(str(record) + '\n')

    def display(self) -> None:
        print("\n--- High Scores ---")
        for record in self.game_record.records:
            print(record)

    def add_record(self, player: Player) -> None:
        self.game_record.add_record(PlayerRecord(player.name, self.file_name, player.score))

