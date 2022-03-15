############------------ IMPORTS ------------############
from importlib.resources import contents
import urwid as uw


############------------ FUNCTION(S) ------------############
def menu_button(caption, callback):
    button = uw.Button(caption)
    uw.connect_signal(button, 'click', callback)
    return uw.AttrMap(
        button, 
        None, 
        focus_map='reversed'
    )


def sub_menu(caption, options):
    contents = menu(caption, options)

    def open_menu(button):
        return top.open_box(contents)
    return menu_button(
        [caption, u'...'],
        open_menu
    )


def menu(title, options):
    body = [uw.Text(title), uw.Divider()]
    body.extend(options)
    return uw.ListBox(
        uw.SimpleFocusListWalker(body)
    )

    
############------------ DRIVER CODE ------------############
