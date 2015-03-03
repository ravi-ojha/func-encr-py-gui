#! /usr/bin/env python
#
# Support module generated by PAGE version 4.5
# In conjunction with Tcl version 8.6
#    Mar 02, 2015 10:38:52 PM


import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

def set_Tk_var():
    # These are Tk variables used passed to Tkinter and must be
    # defined before the widgets using them are created.
    global equality
    equality = StringVar()


def select(p1):
    print('policy_builder_support.select')
    sys.stdout.flush()

def init(top, gui, arg=None):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


