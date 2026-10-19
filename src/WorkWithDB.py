import sqlite3
import os

class WorkWithDB:
    DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), "..", "DB", "auth.db")
    def __init__(self, db_path = None):
        if db_path is None:
            db_path = self.DEFAULT_DB_PATH
        self.con = sqlite3.connect(db_path)

        self.cursor = self.con.cursor()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS AuthLog(
                           Login TEXT NOT NULL,
                           Password TEXT NOT NULL,
                           Repeat_password TEXT NOT NULL,
                           Is_success BOOLEAN NOT NULL,
                           Error TEXT NULL,
                           PRIMARY KEY (Login, Password, Repeat_password)
                           )
        """)
        self.con.commit()

    def add(self, login, password, repeat_password, result, error):
        data = (login,password,repeat_password,result,error)
        self.cursor.execute("INSERT INTO AuthLog (Login, Password, Repeat_password, Is_success, Error) VALUES (?,?,?,?,?)",data)
        self.con.commit()

    def find(self,login,password,repeat_password):
        data = (login,password,repeat_password)
        self.cursor.execute("SELECT * FROM AuthLog WHERE Login = ? AND Password = ? AND Repeat_password = ?", data)
        return self.cursor.fetchone()

    def delete(self, login, password, repeat_password):
        data = (login,password,repeat_password)
        self.cursor.execute("DELETE FROM AuthLog WHERE Login = ? AND Password = ? AND Repeat_password = ?", data)
        self.con.commit()