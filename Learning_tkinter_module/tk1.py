# The tkinter module's purpose is to generate GUIs.

from tkinter import *

# Here, we are creating our class, Window, and inheriting from the Frame class.
# Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
# Then we define the settings upon initialization. This is the master widget.

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

# The above is really all we need to do to get a window instance started.
# Root window created. Here, that would be the only window, but you can later have windows within windows.

root = Tk()

# Then we actually create the instance.

app = Window(root)

# Finally, show it and begin the mainloop.

root.mainloop()

# The above code put together should spawn you a window
