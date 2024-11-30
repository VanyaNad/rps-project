from typing import List, Dict, Any
from game.database import Database


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
        self.db = Database().connect()

    def read_scores(self) -> List[Dict[str, Any]]:
        """Fetches top scores from the database."""
        query = """
            SELECT p.name, m.mode_name, s.score, s.created_at
            FROM scores s
            JOIN players p ON s.player_id = p.id
            JOIN modes m ON s.mode_id = m.id
            ORDER BY s.score DESC;
        """
        with self.db.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def save(self, player_name: str, mode_name: str, score: int) -> None:
        """Saves or updates a player's score in the database."""
        try:
            with self.db.cursor() as cursor:
                # Insert or find player
                cursor.execute("""
                INSERT INTO players (name)
                VALUES (%s)
                ON CONFLICT (name) DO NOTHING
                RETURNING id;
                """, (player_name,))

                result = cursor.fetchone()
                player_id = result['id'] if result and 'id' in result else self._get_player_id(player_name)

                cursor.execute("SELECT id FROM modes WHERE mode_name = %s;", (mode_name,))
                mode_result = cursor.fetchone()
                if not mode_result:
                    raise Exception(f"Mode '{mode_name}' not found in the database.")
                mode_id = mode_result['id']

                cursor.execute("""
                INSERT INTO scores (player_id, mode_id, score)
                VALUES (%s, %s, %s)
                ON CONFLICT (player_id, mode_id)
                DO UPDATE SET score = EXCLUDED.score;
                """, (player_id, mode_id, score))

                self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(f"Error saving score: {e}")

    def clear(self) -> None:
        """Clears all scores from the database."""
        query = """
            DELETE FROM scores;
        """
        with self.db.cursor() as cursor:
            cursor.execute(query)
            self.db.commit()

    def display(self) -> None:
        """Displays the top scores from the database."""
        scores = self.read_scores()
        print("--- Top Scores ---")
        if not scores:
            print("No scores found.")
        else:
            for score in scores:
                print(f"Player: {score['name']}, Mode: {score['mode_name']}, Score: {score['score']}")
        print("\n")

    def _get_player_id(self, player_name: str) -> int:
        """Fetches the player's ID."""
        query = "SELECT id FROM players WHERE name = %s;"
        with self.db.cursor() as cursor:
            cursor.execute(query, (player_name,))
            result = cursor.fetchone()
            if not result:
                raise Exception(f"Player with name '{player_name}' not found.")
            return result['id']
