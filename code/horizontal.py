############------------ IMPORTS ------------############
from subprocess import call
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

############------------ DRIVER CODE ------------############
