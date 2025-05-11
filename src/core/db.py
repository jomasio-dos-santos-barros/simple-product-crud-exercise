import sqlite3
import os


class DBConnectionManager:
    """
    Class to manage the SQLite database connection.

    Attributes:
        db_path (str): Path to the SQLite database file.
        connection (sqlite3.Connection): SQLite connection object.
    Methods:
        connect(): Establish a connection to the database.
        __enter__(): Enter the runtime context related to this object.
        __exit__(exc_type, exc_value, traceback): Exit the runtime context related to this object.
        create_table(): Create the products table if it doesn't exist.
        drop_table(): Drop the products table if it exists.
    """
    def __init__(self, db_path: str = "crud.db"):
        self.db_path = db_path
        self.connection = None
        self.create_table()

    def connect(self):
        """Establish a connection to the database."""
        self.connection = sqlite3.connect(self.db_path)

    def __enter__(self):
        self.connect()
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.commit()
            self.connection.close()

    def create_table(self):
        """Create the products table if it doesn't exist."""
        if not os.path.exists(self.db_path):
            with open(self.db_path, 'w'):
                pass
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL,
                created_at DateTime DEFAULT CURRENT_TIMESTAMP,
                updated_at DateTime DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        self.connection.commit()
        self.connection.close()


    def drop_table(self):
        os.remove(self.db_path)