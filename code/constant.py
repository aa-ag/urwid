from email.mime import base


############------------ IMPORTS ------------############
import urwid as uw


############------------ FUNCTION/CLASS(E/S) ------------############
def ask_question():
    return uw.Pile(
        [uw.Edit(
        ('I say', 
        u"What's your name?"
        )
        )]
    )


def provide_answer():
    return uw.Text(
        ('I say', 
        u"Great meeting you, " + name + "\n"
        )
    )


class ConversationListBox(uw.ListBox):
    def __init__(self):
        body = uw.SimpleFocusListWalker(
            [question()]
        )
        super(ConversationListBox, self).__init__(body)

    def keypress(self, size, key):
        key = super(
            ConversationListBox, self
            ).keypress(size, key)

        if key != 'enter':
            return key

        name = self.focus[0].edit_text
        if not name:
            raise uw.ExitMainLoop()

        # replace / add response
        self.focus.contents[1:] = [
            (answer(name), self.focus.options())
        ]
        position = self.focus_position

        # add new question
        self.body.insert(position + 1, question())
        self.focus_position = position + 1


############------------ DRIVER CODE ------------############
