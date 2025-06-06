from datetime import datetime, timedelta
from dto import CreatePassword, ProfileModel


class PasswordService:
    def __init__(self, repository, crypt, profile: ProfileModel = None):
        self.repository = repository
        self.crypt = crypt
        self.profile = profile

    def create(
            self,
            name: str,
            description: str,
            login: str,
            password: str,
            time_to_change_in_months: int,  #  Time until next password change (in months), 3, 6
    ):
        time_to_change = datetime.now() + timedelta(days=(30 * time_to_change_in_months))
        time_to_change = time_to_change.timestamp()

        profile_id = None
        if self.profile:
            profile_id = self.profile.id

        password = CreatePassword(
            name=name,
            description=description,
            login=login,
            password=password,
            time_to_change=time_to_change,
            profile_id=profile_id,
        )
        self.repository.create(password)

    def get_all(self):
        pass
