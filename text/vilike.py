from talon import Context, Module, actions

ctx = Context()
mod = Module()


@mod.action_class
class Actions:
    def mark(offset: int = 0):
        """set a marker"""
        column = get_column() + offset
        set_marker(column)
        print(column, offset)

    def mark_select(offset: int = 0):
        """select between markers"""
        marker_column = get_marker()
        current_column = get_column() + offset
        if offset > 0:
            go_right(offset)
        elif offset < 0:
            go_left(offset)
        print((marker_column, current_column, offset))
        if current_column > marker_column:
            select_left(current_column - marker_column)
        elif marker_column > current_column:
            select_right(marker_column - current_column)

    def jump(char: str):
        """jump to char"""
        column = find_str(char)
        print(column)
        go_right(column)

    def jump_back(char: str):
        """jump back to char"""
        column = find_str_back(char)
        print(column)
        go_left(column)

    def remove_line():
        """remove line"""
        remove_line()


_marker = None


def get_marker():
    return _marker


def set_marker(column: int):
    global _marker
    _marker = column


def find_str(char: str):
    edit = actions.edit
    edit.extend_line_end()
    text = edit.selected_text()
    go_left()
    print((text, char))
    offset = text.find(char) + len(char)
    return offset


def find_str_back(char: str):
    edit = actions.edit
    edit.extend_line_start()
    text = edit.selected_text()
    go_right()
    print((text, char))
    offset = text.rfind(char)
    return len(text) - offset


def go_left(steps: int = 1):
    edit = actions.edit
    for _ in range(steps):
        edit.left()


def go_right(steps: int = 1):
    edit = actions.edit
    for _ in range(steps):
        edit.right()


def select_left(steps: int):
    edit = actions.edit
    for _ in range(steps):
        edit.extend_left()


def select_right(steps: int):
    edit = actions.edit
    for _ in range(steps):
        edit.extend_right()


def select_down(steps: int):
    edit = actions.edit
    for _ in range(steps):
        edit.extent_down()


def get_cursor_position():
    edit = actions.edit
    edit.extend_file_start()
    text = edit.selected_text()
    go_right()
    n_line_breaks = text.count("\n")
    last_line_break = text.rfind("\n")
    line = n_line_breaks + 1
    column = (len(text) - (last_line_break + 1)) + 1
    return (line, column)


def go_position(position):
    line, column = position
    edit = actions.edit
    edit.jump_line(line)
    go_right(column)


def sort_positions(position1, position2):
    line1, column1 = position1
    line2, column2 = position2
    if line1 > line2:
        return position1, position2
    if line2 > line1:
        return position2, position1
    if column1 > column2:
        return position1, position2
    if column2 > column1:
        return position2, position1
    return position1, position2


def get_column():
    edit = actions.edit
    edit.extend_line_start()
    text = edit.selected_text()
    go_right()
    column = len(text) + 1
    return column


def copy_line():
    edit = actions.edit
    edit.select_line()
    text = edit.selected_text()
    return text


def remove_line():
    edit = actions.edit
    text = copy_line()
    if text and text.strip():
        edit.delete_line()
    text = copy_line()
    if text and not text.strip():
        edit.delete_line()
    text = copy_line()
    if not text:
        actions.key("backspace")
