############------------ IMPORTS ------------############
from ensurepip import bootstrap
import urwid as uw


############------------ FUNCTION(S) ------------############
def menu_button(caption, callback):
    button = uw.Button(caption)
    uw.connect_signal(button, 'click', callback)
    return uw.AttrMap(
        button, 
        None, 
        focus_map='reversed'
    )


def sub_menu(caption, options):
    contents = menu(caption, options)

    def open_menu(button):
        return top.open_box(contents)
    return menu_button(
        [caption, u'...'],
        open_menu
    )


def menu(title, options):
    body = [uw.Text(title), uw.Divider()]
    body.extend(options)
    return uw.ListBox(
        uw.SimpleFocusListWalker(body)
    )


def item_chosen(button):
    response = uw.Text([u'You chose', button.label, u'\n'])
    done = menu_button(u'Ok', exit_program)
    return uw.ListBox(uw.SimpleFocusListWalker(body))


def exit_program(button):
    raise uw.ExitMainLoop()


############------------ GLOBAL VARIABLE(S) ------------############
menu_top = menu(u'Main Menu', [
    sub_menu(u'Applications', [
        sub_menu(u'Accessories', [
            menu_button(u'Text Editor', item_chosen),
            menu_button(u'Terminal', item_chosen),
        ]),
    ]),
    sub_menu(u'System', [
        sub_menu(u'Preferences', [
            menu_button(u'Appearance', item_chosen),
        ]),
        menu_button(u'Lock Screen', item_chosen),
    ]),
])

############------------ DRIVER CODE ------------############
class CascadingBoxes(uw.WidgetPlaceholder):
    max_box_levels = 4

    def __init__(self, box):
        super(CascadingBoxes, self).__init__(uw.SolidFill(u'/'))
        self.box_level = 0
        self.open_box(box)

    def open_box(self, box):
        self.original_widget = uw.Overlay(
            uw.LineBox(box),
            self.original_widget,
            align='center', 
            width=('relative', 80),
            valign='middle', 
            height=('relative', 80),
            min_width=24, 
            min_height=8,
            left=self.box_level * 3,
            right = (self.max_box_levels - self.box_level - 1) * 3,
            top=self.box_level * 2,
            bottom = (self.max_box_levels - self.box_level - 1) * 2
        )
        self.box_level += 1

    def keypress(self, size, key):
        if key == 'esc' and self.box_level > 1:
            self.original_widget = self.original_widget[0]
            self.box_level -= 1
        else:
            return super(CascadingBoxes, self).keypress(size, key)
        

top = CascadingBoxes(menu_top)
uw.MainLoop(top, palette=[('reversed', 'standout', '')]).run()