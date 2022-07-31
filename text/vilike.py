from talon import Context, Module, actions

ctx = Context()
mod = Module()


mod.list(
    'marker',
    desc='marker',
) 

ctx.lists['self.marker'] = {
    'start': 'START',
    'end': 'END',
}


@mod.action_class
class Actions:
    def mark(marker: str, trigram: str):
        """set a marker"""
        p = find_marker(trigram)
        set_marker(marker, p)
        jump(p)
        print((marker, trigram, p))

    def mark_select():
        """select between markers"""
        s = get_marker('START')
        e = get_marker('END')
        print((s, e))
        edit = actions.edit
        jump(s)
        select_right(e + 1 - s)

    def jump(trigram: str):
        """jump to trigram"""
        p = find_marker(trigram)
        jump(p)


_markers = {
    'start': None,
    'end': None,
}    


def get_marker(marker: str):
    return _markers[marker]


def set_marker(marker: str, position: int):
    _markers[marker] = position


def find_marker(trigram: str):
    edit = actions.edit
    go_line_start()
    edit.extend_line_end()
    text = edit.selected_text()    
    p = text.find(trigram)    
    return p


def jump(position: int):
    edit = actions.edit
    go_line_start()
    go_right(position)


def go_line_start():
    edit = actions.edit
    edit.line_start()    
    edit.line_start()


def go_right(steps: int):
    edit = actions.edit
    for _ in range(steps):
        edit.right()
        

def select_right(steps: int):
    edit = actions.edit
    for _ in range(steps):
        edit.extend_right()