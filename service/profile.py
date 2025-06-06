from datetime import datetime, timedelta
from dto import CreateProfile, ProfileModel

class ProfileService:
    def __init__(self, repository, crypt):
        self.repository = repository
        self.crypt = crypt

    def create(
            self,
            title: str,
            description: str = '',
            service_name: str = '',
            email: str = '',
            phone: str = '',
            email_password: str = '',
    ):
        title = self.crypt.crypt(title)
        description = self.crypt.crypt(description)
        service_name = self.crypt.crypt(service_name)
        email = self.crypt.crypt(email)
        phone = self.crypt.crypt(phone)
        email_password = self.crypt.crypt(email_password)

        profile = CreateProfile(
            title=title,
            description=description,
            service_name=service_name,
            email=email,
            phone=phone,
            email_password=email_password
        )
        self.repository.create(profile)

    def get_all(self):
        profiles = self.repository.get_all()
        for i in profiles:
            i.title = self.crypt.decrypt(i.title)
            i.description = self.crypt.decrypt(i.description)
            i.service_name = self.crypt.decrypt(i.service_name)
            i.email = self.crypt.decrypt(i.email)
            i.phone = self.crypt.decrypt(i.phone)
            i.email_password = self.crypt.decrypt(i.email_password)
        return profiles
