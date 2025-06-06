from abc import ABC, abstractmethod


class AbstractServiceAdapter(ABC):
    @abstractmethod
    def get_data(self):
        raise NotImplementedError

    @abstractmethod
    def get_column_name(self):
        raise NotImplementedError


class ProfileTableServiceAdapter(AbstractServiceAdapter):
    def __init__(self, service) -> None:
        self.service = service

    def get_data(self):
        profiles = []
        for i in self.service.get_all():
            profiles.append(
                (
                    str(i.id),
                    str(i.title),
                    str(i.service_name),
                    str(i.email),
                    str(i.phone),
                )
            )
        return profiles

    def get_column_name(self):
        return ['id', 'title', 'service name', 'email', 'phone']

    def insert(self, *args, **kargs):
        self.service.create(
            *args, **kargs
        )

    def copy(self, pos):
        with open('test', 'w') as f:
            data = self.get_data()
            f.write(str(data[pos]))


class PasswordTableServiceAdapter(AbstractServiceAdapter):
    def __init__(self, service) -> None:
        self.service = service

    def get_data(self):
        profiles = []
        for i in self.service.get_all():
            profiles.append(
                (
                    str(i.id),
                    str(i.name),
                    str(i.description),
                    str(i.login),
                    str(i.password),
                    str(i.time_to_change),
                    str(i.extra),
                    str(i.profile_id),
                )
            )
        return profiles

    def get_column_name(self):
        return ['id', 'name', 'description', 'login', 'password', 'time_to_change', 'extra', 'profile_id']

    def copy(self, pos):
        with open('test', 'w') as f:
            data = self.get_data()
            f.write(str(data[pos]))
