############------------ IMPORTS ------------############
import urwid as uw


############------------ GLOBAL VARIABLE(S) ------------############


############------------ FUNCTION(S) ------------############
def exit_on_q(key):
    if key in ('q', 'Q'):
        raise uw.ExitMainLoop()

palette = [
    ('banner', 'black', 'light gray'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue'),
]


text = uw.Text(('banner', u'Hello World'), align='center')
map1 = uw.AttrMap(text, 'streak')
fill = uw.Filler(map1)
map2 = uw.AttrMap(fill, 'bg')
loop = uw.MainLoop(map2, palette, unhandled_input=exit_on_q)
loop.run()