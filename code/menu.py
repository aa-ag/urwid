############------------ IMPORTS ------------############
import urwid as uw

############------------ GLOBAL VARIABLE(S) ------------############
options = u'A B C D'.split()


############------------ FUNCTION(S) ------------############
def menu(title, options):
    body = [uw.Text(title), uw.Divider()]
    for option in options:
        button = uw.Button(option)
        uw.connect_signal(
            button, 
            'click', 
            item_chosen, 
            option
        )
        body.append(uw.AttrMap(
            button,
            None,
            focus_map='reversed'
        ))
    return uw.ListBox(uw.SimpleFocusListWalker(body))


def item_chosen(button, option):
    response = uw.Text(
        [u'You chose',
        option, 
        u'\n']
    )
    done = uw.Button(u'Ok')
    uw.connect_signal(
        done, 
        'click',
        exit_program
    )
    main.original_widget = uw.Filler(uw.Pile(
        response,
        uw.AttrMap(done, None, focus_map='reversed')
    ))


def exit_program(button):
    return uw.ExitMainLoop()


############------------ DRIVER CODE ------------############
main = uw.Padding(
    menu(u'Options\'s Menu', options),
    left=2,
    right=2
)

top = uw.Overlay(
    main,
    uw.SolidFill(u'\N{MEDIUM SHADE}'),
    align='center',
    width=('relative', 60),
    valign='middle',
    height=('relative', 60),
    min_width=20,
    min_height=9
)

uw.MainLoop(top, palette=[(
    'reversed', 'standout', ''
)]).run()