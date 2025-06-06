import os
import sqlite3
from db.querys import CREATE_DATABASE_PASSWORDS, CREATE_DATABASE_PROFILE
import config


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    _cursor = None
    _connection = None

    def __init__(self, name) -> None:
        self.name = name
        self.path_to_db = os.path.join(config.DATABASES_PATH, name)

    def get_cursor(self):
        if self._cursor is not None:
            return self._connection, self._cursor

        if not os.path.exists(self.path_to_db):
            print('database not exists')
            exit(0)

        self._connection = sqlite3.connect(self.path_to_db)
        self._cursor = self._connection.cursor()
        return self._connection, self._cursor

    def create_database(self):
        con = sqlite3.connect(self.path_to_db)
        cursor = con.cursor()
        cursor.execute(CREATE_DATABASE_PASSWORDS)
        cursor.execute(CREATE_DATABASE_PROFILE)
        con.close()
