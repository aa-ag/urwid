############------------ IMPORTS ------------############
import urwid as uw


############------------ FUNCTION(S) ------------############
def exit_on_q(key):
    if key in ('q', 'Q'):
        raise uw.ExitMainLoop()

class QuestionBox(uw.Filler):
    def keypress(self, size, key):
        if key != 'enter':
            return super(
                QuestionBox, self
            ).keypress(
                size, key
            )
        self.original_widget = uw.Text(
            u"Nice to meet you,\n%s.\n\nPress Q/q to exit." % edit.edit_text
        )
