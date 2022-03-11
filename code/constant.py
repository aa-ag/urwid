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
    pass


############------------ DRIVER CODE ------------############
