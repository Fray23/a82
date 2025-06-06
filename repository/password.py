from dto import CreatePassword, PasswordModel

class PasswordRepository:
    def __init__(self, database):
        self.database = database

    def create(self, password: CreatePassword):
        conn, cursor = self.database.get_cursor()
        cursor.execute(
            'INSERT INTO passwords (name, description, login, password, time_to_change, profile_id)'
            'values (?, ?, ?, ?, ?, ?);',
            (password.name,
             password.description,
             password.login,
             password.password,
             password.time_to_change,
             password.profile_id)
        )
        conn.commit()

    def get_all(self):
        _, cursor = self.database.get_cursor()
        cursor.execute('SELECT id, name, description, login, password, time_to_change, extra, profile_id FROM passwords')
        rows = cursor.fetchall()
        passwords = [
            PasswordModel(
                id=row[0],
                name=row[1],
                description=row[2],
                login=row[3],
                password=row[4],
                time_to_change=row[5],
                extra=row[6],
                profile_id=row[7]
            )
            for row in rows
        ]
        return passwords
