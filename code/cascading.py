############------------ IMPORTS ------------############
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
