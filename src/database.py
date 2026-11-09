import sqlite3
import os

class Database:
    DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), "..", "DB", "auth.db")
    def __init__(self, db_path=None):
        if db_path is None:
            db_path = self.DEFAULT_DB_PATH
        self.con = sqlite3.connect(db_path)

        self.cursor = self.con.cursor()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS comments(
                               id INTEGER PRIMARY KEY,
                               name TEXT NOT NULL,
                               message TEXT NOT NULL
                               )
            """)
        self.con.commit()

    def get_by_id(self, id_com):
        self.cursor.execute("SELECT * FROM comments WHERE id = ?", [id_com])
        return self.cursor.fetchone()

    def get_by_name(self, user_name):
        self.cursor.execute("SELECT * FROM comments WHERE name = ?", [user_name])
        return self.cursor.fetchall()

    def add(self, id_com: int, user_name : str, message: str):
        try:
            if id_com < 0:
                return False
            if len(user_name) > 256:
                return  False
            if len(message) > 8096:
                return False
            data = [id_com,user_name,message]
            self.cursor.execute("INSERT INTO comments (id, name, message) VALUES (?,?,?)",data)
            self.con.commit()
            return True
        except(ValueError, TypeError, sqlite3.Error):
            return False

    def update(self, id_com, new_message : str):
        try:
            if len(new_message) > 8096:
                return False
            data = [new_message,id_com]
            self.cursor.execute("UPDATE comments SET message = ? WHERE id = ?", data)
            return True
        except sqlite3.Error:
            return False
