############------------ IMPORTS ------------############
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


############------------ DRIVER CODE ------------############
