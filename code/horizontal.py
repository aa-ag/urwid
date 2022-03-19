############------------ IMPORTS ------------############
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


class Choice(uw.WidgetWrap):
    def __init__(self, caption):
        super(Choice, self).__init__(
            MenuButton(caption, self.item_chosen)
        )
        self.caption = caption

    def item_chosen(self, button):
        response = uw.Text([u'  You chose ', self.caption, u'\n'])
        done = MenuButton(u'Ok', exit_program)
        response_box = uw.Filler(uw.Pile([response, done]))
        top.open_box(uw.AttrMap(response_box, 'options'))


def exit_program(key):
    raise uw.ExitMainLoop()


menu_top = SubMenu(u'Main Menu', [
    SubMenu(u'Applications', [
        SubMenu(u'Accessories', [
            Choice(u'Text Editor'),
            Choice(u'Terminal'),
        ]),
    ]),
    SubMenu(u'System', [
        SubMenu(u'Preferences', [
            Choice(u'Appearance'),
        ]),
        Choice(u'Lock Screen'),
    ]),
])

palette = [
    (None,  'light gray', 'black'),
    ('heading', 'black', 'light gray'),
    ('line', 'black', 'light gray'),
    ('options', 'dark gray', 'black'),
    ('focus heading', 'white', 'dark red'),
    ('focus line', 'black', 'dark red'),
    ('focus options', 'black', 'light gray'),
    ('selected', 'white', 'dark blue')]

focus_map = {
    'heading': 'focus heading',
    'options': 'focus options',
    'line': 'focus line'
}

class HorizontalBoxes(uw.Columns):
    def __init__(self):
        super(HorizontalBoxes, self).__init__([], dividechars=1)

    def open_box(self, box):
        if self.contents:
            del self.contents[self.focus_position + 1:]
        self.contents.append((uw.AttrMap(box, 'options', focus_map),
            self.options('given', 24)))

        self.focus_position = len(self.contents) - 1


############------------ DRIVER CODE ------------############
top = HorizontalBoxes()
top.open_box(menu_top.menu)
uw.MainLoop(uw.Filler(top, 'middle', 10), palette).run()