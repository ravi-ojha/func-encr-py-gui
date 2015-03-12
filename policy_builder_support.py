#! /usr/bin/env python

from Tkinter import *

import sys
import ttk

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


