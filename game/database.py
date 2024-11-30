import psycopg2
from psycopg2.extras import RealDictCursor
from game.settings import DB_CONFIG


# Connect to the DB using Singleton
class Database:
    _instance = None  # Singleton instance of the Database
    _connection = None  # Active database connection

    def __new__(cls, *args, **kwargs) -> "Database":
        """
        Creates or retrieves the singleton instance of the Database class
        """
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def connect(self) -> psycopg2.extensions.connection:
        """
        Establishes a connection to the database if one does not already exist

        Returns:
            psycopg2.extensions.connection: The active database connection
        """
        if not self._connection:
            self._connection = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
        return self._connection

    def close(self) -> None:
        """
        Closes the database connection if it is open.
        """
        if self._connection:
            self._connection.close()
            self._connection = None
