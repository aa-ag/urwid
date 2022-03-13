from email.mime import base


############------------ IMPORTS ------------############
import urwid as uw

############------------ GLOBAL VARIABLE(S) ------------############
options = u'A B C D'.split()


############------------ FUNCTION(S) ------------############
def menu(title, options):
    body = [uw.Text(title), uw.Divider()]
    for option in options:
        button = uw.Button(option)
        uw.connect_signal(
            button, 
            'click', 
            item_chosen, 
            option
        )
        body.append(uw.AttrMap(
            button,
            None,
            focus_map='reversed'
        ))
    return uw.ListBox(uw.SimpleFocusListWalker(body))


def item_chosen():
    pass


def exit_program(button):
    return uw.ExitMainLoop()


############------------ DRIVER CODE ------------############
