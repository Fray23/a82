from dto import CreateProfile, CreatePassword, ProfileModel, PasswordModel

class ProfileRepository:
    def __init__(self, database):
        self.database = database

    def get_all(self):
        _, cursor = self.database.get_cursor()
        cursor.execute('SELECT id, title, description, service_name, email, phone, email_password FROM profile')
        rows = cursor.fetchall()
        profiles = [
            ProfileModel(
                id=row[0],
                title=row[1],
                description=row[2],
                service_name=row[3],
                email=row[4],
                phone=row[5],
                email_password=row[6]
            )
            for row in rows
        ]
        return profiles

    def create(self, profile: CreateProfile):
        conn, cursor = self.database.get_cursor()
        cursor.execute(
            'INSERT INTO profile (title, description, service_name, email, phone, email_password)'
            'values (?, ?, ?, ?, ?, ?);',
            (profile.title,
             profile.description,
             profile.service_name,
             profile.email,
             profile.phone,
             profile.email_password)
        )
        conn.commit()

    def get(self, id):
        try:
            id = int(id)
        except:
            return None

        for p in self.get_all():
            if p.id == id:
                return p
        return None
