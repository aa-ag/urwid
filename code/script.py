############------------ IMPORTS ------------############
import urwid as uw


############------------ GLOBAL VARIABLE(S) ------------############
palette = [('I say', 'default,bold', 'default', 'bold'),]
ask = uw.Edit(('I say', u"What is your name?\n"))
reply = uw.Text(u"")
button = uw.Button(u'Exit')
div = uw.Divider()
pile = uw.Pile([ask, div, reply, div, button])
top = uw.Filler(pile, valign='top')


############------------ FUNCTION(S) ------------############
def on_ask_change(edit, new_edit_text):
    reply.set_text(
        ('I say', u"Nice to meet you, %s" % new_edit_text)
    )


def on_exit_clicked(button):
    raise uw.ExitMainLoop()
    

############------------ DRIVER CODE ------------############
