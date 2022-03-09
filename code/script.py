############------------ IMPORTS ------------############
import urwid as uw


############------------ GLOBAL VARIABLE(S) ------------############


############------------ FUNCTION(S) ------------############
def exit_on_q(key):
    if key in ('q', 'Q'):
        raise uw.ExitMainLoop()

palette = [
    ('banner', '', '', '', '#ffa', '#60d'),
    ('streak', '', '', '', 'g50', '#60a'),
    ('inside', '', '', '', 'g38', '#808'),
    ('outside', '', '', '', 'g27', '#a06'),
    ('bg', '', '', '', 'g7', '#d06'),
]


placeholder = uw.SolidFill()
loop = uw.MainLoop(placeholder, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
loop.widget = uw.AttrMap(placeholder, 'bg')
loop.widget.original_widget = uw.Filler(uw.Pile([]))

div = uw.Divider()
outside = uw.AttrMap(div, 'outside')
inside = uw.AttrMap(div, 'inside')
txt = uw.Text(('banner', u" Hello World "), align='center')
streak = uw.AttrMap(txt, 'streak')
pile = loop.widget.base_widget # .base_widget skips the decorations
for item in [outside, inside, streak, inside, outside]:
    pile.contents.append((item, pile.options()))


loop.run()