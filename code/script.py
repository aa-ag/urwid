############------------ IMPORTS ------------############
import urwid as uw


############------------ GLOBAL VARIABLE(S) ------------############


############------------ FUNCTION(S) ------------############
def show_or_exit(key):
    if key in ('q', 'Q'):
        raise uw.ExitMainLoop()
    text.set_text(repr(key))


text = uw.Text(u'Hello World')
fill = uw.Filler(text, 'top')
loop = uw.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()