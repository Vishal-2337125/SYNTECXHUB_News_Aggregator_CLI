import sqlite3
import pandas as pd

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS news (headline TEXT, url TEXT PRIMARY KEY)')

    def save(self, data):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.executemany('INSERT OR IGNORE INTO news VALUES (:headline, :url)', data)
            return cursor.rowcount

    def get_as_df(self):
        with sqlite3.connect(self.db_name) as conn:
            return pd.read_sql_query("SELECT * FROM news", conn)