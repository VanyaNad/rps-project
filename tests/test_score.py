import unittest
from game.score import PlayerRecord
from game.score import ScoreHandler
from unittest.mock import patch, MagicMock


class TestPlayerRecord(unittest.TestCase):
    def setUp(self):
        self.records = [
            PlayerRecord(name="Alice", mode="Normal", score=100),
            PlayerRecord(name="Bob", mode="Hard", score=200),
            PlayerRecord(name="Eve", mode="Normal", score=0),
        ]

    def test_initialization(self):
        for record, data in zip(self.records, [("Alice", "Normal", 100), ("Bob", "Hard", 200), ("Eve", "Normal", 0)]):
            self.assertEqual(record.name, data[0])
            self.assertEqual(record.mode, data[1])
            self.assertEqual(record.score, data[2])

    def test_high_score_values(self):
        record = PlayerRecord(name="Alice", mode="Normal", score=1_000_000)
        self.assertEqual(record.score, 1_000_000)



    def test_score_comparison(self):
        self.assertGreater(self.records[1].score, self.records[0].score)
        self.assertLess(self.records[0].score, self.records[1].score)
        self.assertEqual(self.records[2].score, 0)

    def test_record_equality(self):
        record1 = PlayerRecord(name="Alice", mode="Normal", score=100)
        record2 = PlayerRecord(name="Alice", mode="Normal", score=100)
        self.assertEqual(record1.name, record2.name)
        self.assertEqual(record1.score, record2.score)

class TestScoreHandlerInitialization(unittest.TestCase):
    @patch('game.database.Database.connect')
    def test_initialization(self, mock_connect):
        mock_db_connection = MagicMock()
        mock_connect.return_value = mock_db_connection

        handler = ScoreHandler()

        mock_connect.assert_called_once()
        self.assertEqual(handler.db, mock_db_connection)


if __name__ == "__main__":
    unittest.main()
