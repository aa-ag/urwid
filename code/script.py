############------------ IMPORTS ------------############
import urwid as uw


############------------ GLOBAL VARIABLE(S) ------------############


############------------ FUNCTION(S) ------------############
def testing_stuff():
    text = uw.Text(u'Hello World')
    fill = uw.Filler(text, 'top')
    loop = uw.MainLoop(fill)
    loop.run()

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    testing_stuff()