#! /usr/bin/env python
# GUI was generated using PAGE v4.5 in conjuction with Tcl v8.6

from Tkinter import *

import sys
import ttk

import policy_builder
import boolean_logic_builder
import create_policy_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('New_Toplevel_1')
    geom = "607x458+478+164"
    root.geometry(geom)
    w = New_Toplevel_1 (root)
    create_policy_support.init(root, w)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('New_Toplevel_1')
    geom = "607x458+478+164"
    w.geometry(geom)
    w_win = New_Toplevel_1 (w)
    create_policy_support.init(w, w_win, param)
    return w_win

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        master.configure(highlightcolor="black")


        self.Frame1 = Frame(master)
        self.Frame1.place(relx=0.05, rely=0.07, relheight=0.86, relwidth=0.9)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="1")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#e5e5e5")
        self.Frame1.configure(width=545)

        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.28, rely=0.2, relheight=0.06, relwidth=0.47)
        self.Message1.configure(text='''Policy Builder Wizard''')
        self.Message1.configure(width=255)

        self.bBuildPolicy = Button(self.Frame1)
        self.bBuildPolicy.place(relx=0.2, rely=0.63, height=27, width=94)
        self.bBuildPolicy.configure(activebackground="#d9d9d9")
        self.bBuildPolicy.configure(text='''Build Policy''')
        self.bBuildPolicy.bind("<Button-1>",self.onBuildPolicyClick)

        self.bViewPolicy = Button(self.Frame1)
        self.bViewPolicy.place(relx=0.62, rely=0.63, height=27, width=92)
        self.bViewPolicy.configure(activebackground="#d9d9d9")
        self.bViewPolicy.configure(text='''View Policy''')
        #self.bViewPolicy.bind("<Button-1>",self.onViewPolicyClick)

    def onBuildPolicyClick(self, event):
        global root
        policy_builder.create_New_Toplevel_1(root)




if __name__ == '__main__':
    vp_start_gui()



