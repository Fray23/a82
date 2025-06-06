import curses


class Table():
    def __init__(self, win, model):
        self.win = win
        self.model = model
        self.fields_names = self.model.get_column_name()

        self.cursor_pos = 0

    def draw(self):
        data = self.model.get_data()
        width = self._calculate_width(data)

        self._draw_header(width)
        self._draw_border(1, width)
        self._draw_raw(2, width, data)
        self._draw_border(2 + len(data), width)

    def _calculate_width(self, rows):
        rows = rows.copy()
        rows.append(self.fields_names)
        return tuple(max(len(row[i]) for row in rows) for i in range(len(rows[0])))

    def _draw_header(self, column_size):
        line = self._format_line(self.fields_names, column_size)
        self.safe_addstr(0, 0, line)

    def _draw_border(self, y, column_size):
        line = '+'
        for i in column_size:
            line += '-' * i
            line += '+'
        self.safe_addstr(y, 0, line)

    def _draw_raw(self, y, width, data):
        for i, row in enumerate(data):
            line = self._format_line(row, width)
            attr = curses.color_pair(1) | curses.A_REVERSE if i == self.cursor_pos else curses.color_pair(1)
            self.safe_addstr(y, 0, line, attr)
            y += 1

    def safe_addstr(self, y, x, text, attr=0):
        height, width = self.win.getmaxyx()
        max_len = width - x
        if max_len <= 0 or y >= height:
            return
        self.win.addstr(y, x, text[:max_len], attr)

    @staticmethod
    def _format_line(items, widths):
        assert len(items) == len(widths)

        format_parts = []
        for width in widths:
            format_parts.append(f"{{:<{width}}}")

            line_format = "|".join(format_parts)
            line_format = f"|{line_format}|"

        return line_format.format(*items)

    def move_cursor_down(self):
        if self.cursor_pos < len(self.model.get_data()) - 1:
            self.cursor_pos += 1

    def move_cursor_up(self):
        if self.cursor_pos > 0:
            self.cursor_pos -= 1
