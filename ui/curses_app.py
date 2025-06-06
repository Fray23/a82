import curses
from ui.enum import SIGNALS


class UI:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def setup_colors(self):
        curses.use_default_colors()
        curses.init_pair(1, 255, -1)

    def input_dialog(self, prompt):
        height, width = self.stdscr.getmaxyx()
        win = curses.newwin(3, width - 4, height // 2, 2)
        win.border()
        win.addstr(1, 2, prompt)
        win.refresh()
        curses.echo()
        input_str = win.getstr(1, len(prompt) + 2).decode("utf-8")
        curses.noecho()
        return input_str.strip()

    def clear(self):
        self.stdscr.clear()

    def refresh(self):
        self.stdscr.refresh()

    def get_input(self):
        return self.stdscr.getch()


class CursesApp:
    def __init__(self, stdscr, controller_factory):
        self.ui = UI(stdscr)
        self.controller_stack = [controller_factory.get_profile_controller(self.ui)]
        self.controller_factory = controller_factory

    def start(self):
        self.ui.setup_colors()

        while self.controller_stack:
            self.ui.clear()
            self.controller_stack[-1].render()
            self.ui.refresh()
            key = self.ui.get_input()
            signal, info = self.controller_stack[-1].handle_key(key)

            if signal == SIGNALS.EXIT:
                self.controller_stack.pop()

            if signal == SIGNALS.OPEN_PASSWORD_SCREEN:
                profile_id = info.get('profile_id')
                new_controller = self.controller_factory.get_password_controller(self.ui)
                self.controller_stack.append(new_controller)
