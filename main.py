import curses
from ui.curses_app import CursesApp
from ui.factorys import ControllerFactory

from db.connection import Database
from util.crypt import Cipher

database = Database(name='test')
database.create_database()


cipher = Cipher('xxElfC01')
profile = None


def run_curses_app():
    def app(stdscr):
        app = CursesApp(stdscr, ControllerFactory(database, cipher))
        app.start()

    curses.wrapper(app)

run_curses_app()
