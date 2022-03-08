import urwid as uw

text = uw.Text(u'Hello World')
fill = uw.Filler(text, 'top')
loop = uw.MainLoop(fill)
loop.run()