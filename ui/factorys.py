from repository import PasswordRepository, ProfileRepository
from service import PasswordService, ProfileService
from ui.controller import ProfileController, PasswordController
from ui.adapters import ProfileTableServiceAdapter


class ControllerFactory:
    def __init__(self, db, crypt) -> None:
        self.db = db
        self.crypt = crypt

    def get_profile_controller(self, ui):
        repository = ProfileRepository(self.db)
        service = ProfileService(repository, self.crypt)
        adapter_service = ProfileTableServiceAdapter(service)
        return ProfileController(ui=ui, service=adapter_service)

    def get_password_controller(self, ui):
        # repository = PasswordRepository(database=self.db)
        # repository = (repository)
        # return PasswordController(ui=ui, repository=repository)
        pass
