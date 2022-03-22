############------------ IMPORTS ------------############
import urwid as uw


############------------ GLOBAL VARIABLE(S) ------------############


############------------ FUNCTION(S) ------------############
class ActionButton(uw.Button):
    def __init__(self, caption, callback):
        super(ActionButton, self).__init__("")
        uw.connect_signal(self, 'click', callback)
        self._w = uw.AttrMap(uw.SelectableIcon(caption, 1),
            None, focus_map='reversed')


class Place(uw.WidgetWrap):
    def __init__(self, name, choices):
        super(Place, self).__init__(
            ActionButton([u" > go to ", name], self.enter_place))
        self.heading = uw.Text([u"\nLocation: ", name, "\n"])
        self.choices = choices
        for child in choices:
            getattr(child, 'choices', []).insert(0, self)
        

    def enter_place(self, button):
        game.update_place(self)


class Thing(uw.WidgetWrap):
    def __init__(self, name):
        super(Thing, self).__init__(
            ActionButton([u" * take ", name], self.take_thing))
        self.name = name

    def take_thing(self, button):
        self._w = uw.Text(u" - %s (taken)" % self.name)
        game.take_thing(self)


def exit_program(button):
    raise uw.ExitMainLoop()

############------------ DRIVER CODE ------------############
