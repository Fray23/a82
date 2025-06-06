import curses
from ui.table import Table
from ui.enum import SIGNALS


class BaseController():
    def __init__(self, ui, service):
        self.ui = ui
        self.service = service
        self.table = Table(ui.stdscr, service)

    def render(self):
        self.table.draw()

    def handle_key(self, key):
        if key == ord('q'):
            return SIGNALS.EXIT, None

        if key == ord('j'):
            self.table.move_cursor_down()

        if key == ord('k'):
            self.table.move_cursor_up()

        return SIGNALS.PASS, None


class ProfileController(BaseController):
    def insert_profile(self):
        title = self.ui.input_dialog('title:')
        service_name = self.ui.input_dialog('service_name:')
        email = self.ui.input_dialog('email:')
        phone = self.ui.input_dialog('phone:')
        self.service.insert(
            title,
            service_name,
            email,
            phone,
        )

    def handle_key(self, key):
        if key == ord('o'):
            id = self.table.cursor_pos
            profile_id = self.service.get_data()[id][0]

            return (
                SIGNALS.OPEN_PASSWORD_SCREEN,
                {
                    "profile_id": profile_id
                }
            )

        if key == ord('i'):
            self.insert_profile()

        return super().handle_key(key)

class PasswordController(BaseController):
    def handle_key(self, key):
        if key == ord('i'):
            self.ui.input_dialog('test:')

        return super().handle_key(key)
