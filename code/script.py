############------------ IMPORTS ------------############
import urwid as uw


############------------ GLOBAL VARIABLE(S) ------------############


############------------ FUNCTION(S) ------------############
def exit_on_q(key):
    if key in ('q', 'Q'):
        raise uw.ExitMainLoop()