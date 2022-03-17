############------------ IMPORTS ------------############
from subprocess import call
from tkinter import Listbox
import urwid as uw


############------------ FUNCTION(S) ------------############
class MenuButton(uw.Button):
    def __init__(self, caption, callback):
        super(MenuButton, self).__init__("")
        uw.connect_signal(self, 'click', callback)
        self._w = uw.AttrMap(uw.SelectableIcon(
            [u' \N{BULLET} ', caption], 
            2), 
            None, 
            'selected'
        )


class SubMenu(uw.WidgetWrap):
    def __init__(self, caption, choices):
        super(SubMenu, self).__init__(MenuButton(
            [caption, 
            u'\N{HORIZONTAL ELLIPSIS}'],
            self.open_menu
        ))
        line = uw.Divider(u'\N{LOWER ONE QUARTER BLOCK}')
        listbox = uw.ListBox(uw.SimpleFocusListWalker([
            uw.AttrMap(uw.Text([u"\n  ", caption]), 'heading'),
            uw.AttrMap(line, 'line'),
            uw.Divider()] + choices + [uw.Divider()]))

        self.menu = uw.AttrMap(listbox, 'options')

############------------ DRIVER CODE ------------############
