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

    def open_menu(self, button):
        top.open_box(self.menu)

palette = [
    (None,  'light gray', 'black'),
    ('heading', 'black', 'light gray'),
    ('line', 'black', 'light gray'),
    ('options', 'dark gray', 'black'),
    ('focus heading', 'white', 'dark red'),
    ('focus line', 'black', 'dark red'),
    ('focus options', 'black', 'light gray'),
    ('selected', 'white', 'dark blue')]

class HorizontalBoxes(uw.Columns):
    def __init__(self):
        super(HorizontalBoxes, self).__init__([], dividechars=1)

    def open_boxes(self, box):
        if self.contents:
            del self.contents[self.focus_position + 1:]
        self.contents.append((uw.AttrMap(box, 'options', focus_map),
            self.options('given', 24)))

        self.focus_position = len(self.contents) - 1


############------------ DRIVER CODE ------------############
top = HorizontalBoxes()
top.open_box(menu_top.menu)
uw.MainLoop(uw.Filler(top, 'miller', 10), palette).run()