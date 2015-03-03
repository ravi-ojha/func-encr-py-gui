#! /usr/bin/env python
# GUI was generated using PAGE v4.5 in conjuction with Tcl v8.6

from Tkinter import *

import sys
import ttk

import policy_builder_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('New_Toplevel_1')
    geom = "600x608+454+106"
    root.geometry(geom)
    policy_builder_support.set_Tk_var()
    w = New_Toplevel_1 (root)
    policy_builder_support.init(root, w)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('New_Toplevel_1')
    geom = "600x608+454+106"
    w.geometry(geom)
    policy_builder_support.set_Tk_var()
    w_win = New_Toplevel_1 (w)
    policy_builder_support.init(w, w_win, param)
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

        self.attrList = ["Name","Designation","Department","Joining Date"]

        self.dataSelectionFrame = Frame(master)
        self.dataSelectionFrame.place(relx=0.05, rely=0.05, relheight=0.49, relwidth=0.89)
        self.dataSelectionFrame.configure(relief=GROOVE)
        self.dataSelectionFrame.configure(borderwidth="1")
        self.dataSelectionFrame.configure(relief=GROOVE)
        self.dataSelectionFrame.configure(background="#e5e5e5")
        self.dataSelectionFrame.configure(width=535)

        self.lbAttributes = Listbox(self.dataSelectionFrame)
        self.lbAttributes.place(relx=0.04, rely=0.1, relheight=0.83, relwidth=0.42)
        self.lbAttributes.configure(background="white")
        self.lbAttributes.configure(borderwidth="0")
        self.lbAttributes.configure(font="TkFixedFont")
        self.lbAttributes.configure(selectbackground="#c4c4c4")

        for attr in self.attrList:
            self.lbAttributes.insert(END,attr)

        self.attrDict = {}
        for attr in self.attrList:
            self.attrDict[attr] = ["",""]

        self.lbAttributes.select_set(0) #This only sets focus on the first item.
        self.lbAttributes.event_generate("<<ListboxSelect>>")
        self.lbAttributes.bind("<<ListboxSelect>>", self.onSelect)

        self.attrVal = StringVar()
        self.attrValTextBox = Entry(self.dataSelectionFrame)
        self.attrValTextBox.place(relx=0.5, rely=0.17, relheight=0.14, relwidth=0.44)
        self.attrValTextBox.configure(background="white")
        self.attrValTextBox.configure(font="TkFixedFont")
        self.attrValTextBox.configure(selectbackground="#c4c4c4")
        self.attrValTextBox.configure(textvariable=self.attrVal)

        self.varAttr = StringVar()
        self.varAttr.set("Select attribute from left")
        self.Label1 = Label(self.dataSelectionFrame)
        self.Label1.place(relx=0.56, rely=0.1, height=19, width=176)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(textvariable=self.varAttr)

        self.bOk = Button(self.dataSelectionFrame)
        self.bOk.place(relx=0.65, rely=0.54, height=27, width=62)
        self.bOk.configure(activebackground="#d9d9d9")
        self.bOk.configure(text='''Ok''')
        self.bOk.bind("<Button-1>",self.onOkClick)

        self.Label3 = Label(self.dataSelectionFrame)
        self.Label3.place(relx=0.04, rely=0.03, height=19, width=224)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''Available Attributes''')
        self.Label3.configure(width=224)

        self.rbEE = Radiobutton(self.dataSelectionFrame)
        self.rbEE.place(relx=0.56, rely=0.34, relheight=0.07
                , relwidth=0.07)
        self.rbEE.configure(activebackground="#d9d9d9")
        self.rbEE.configure(background="#e5e5e5")
        self.rbEE.configure(borderwidth="0")
        self.rbEE.configure(highlightthickness="0")
        self.rbEE.configure(justify=LEFT)
        self.rbEE.configure(text='''=''')
        self.rbEE.configure(value=" = ")
        self.rbEE.configure(variable=policy_builder_support.equality)
        self.rbEE.configure(width=40)
        self.rbEE.invoke()

        self.rbLE = Radiobutton(self.dataSelectionFrame)
        self.rbLE.place(relx=0.67, rely=0.34, relheight=0.06
                , relwidth=0.08)
        self.rbLE.configure(activebackground="#d9d9d9")
        self.rbLE.configure(background="#e5e5e5")
        self.rbLE.configure(borderwidth="0")
        self.rbLE.configure(highlightthickness="0")
        self.rbLE.configure(justify=LEFT)
        self.rbLE.configure(text='''<=''')
        self.rbLE.configure(value=" <= ")
        self.rbLE.configure(variable=policy_builder_support.equality)

        self.rbGE = Radiobutton(self.dataSelectionFrame)
        self.rbGE.place(relx=0.8, rely=0.34, relheight=0.06
                , relwidth=0.08)
        self.rbGE.configure(activebackground="#d9d9d9")
        self.rbGE.configure(background="#e5e5e5")
        self.rbGE.configure(borderwidth="0")
        self.rbGE.configure(highlightthickness="0")
        self.rbGE.configure(justify=LEFT)
        self.rbGE.configure(text='''>=''')
        self.rbGE.configure(value=" >= ")
        self.rbGE.configure(variable=policy_builder_support.equality)

        self.rbLT = Radiobutton(self.dataSelectionFrame)
        self.rbLT.place(relx=0.67, rely=0.44, relheight=0.07
                , relwidth=0.09)
        self.rbLT.configure(activebackground="#d9d9d9")
        self.rbLT.configure(background="#e5e5e5")
        self.rbLT.configure(borderwidth="0")
        self.rbLT.configure(highlightthickness="0")
        self.rbLT.configure(justify=LEFT)
        self.rbLT.configure(text='''<''')
        self.rbLT.configure(value=" < ")
        self.rbLT.configure(variable=policy_builder_support.equality)

        self.rbGT = Radiobutton(self.dataSelectionFrame)
        self.rbGT.place(relx=0.8, rely=0.44, relheight=0.07
                , relwidth=0.09)
        self.rbGT.configure(activebackground="#d9d9d9")
        self.rbGT.configure(background="#e5e5e5")
        self.rbGT.configure(borderwidth="0")
        self.rbGT.configure(highlightthickness="0")
        self.rbGT.configure(justify=LEFT)
        self.rbGT.configure(text='''>''')
        self.rbGT.configure(value=" > ")
        self.rbGT.configure(variable=policy_builder_support.equality)

        self.rbNE = Radiobutton(self.dataSelectionFrame)
        self.rbNE.place(relx=0.56, rely=0.44, relheight=0.06
                , relwidth=0.08)
        self.rbNE.configure(activebackground="#d9d9d9")
        self.rbNE.configure(background="#e5e5e5")
        self.rbNE.configure(highlightthickness="0")
        self.rbNE.configure(justify=LEFT)
        self.rbNE.configure(text='''!=''')
        self.rbNE.configure(value=" != ")
        self.rbNE.configure(variable=policy_builder_support.equality)

        self.dataDisplayFrame = Frame(master)
        self.dataDisplayFrame.place(relx=0.05, rely=0.61, relheight=0.35, relwidth=0.89)
        self.dataDisplayFrame.configure(relief=GROOVE)
        self.dataDisplayFrame.configure(borderwidth="2")
        self.dataDisplayFrame.configure(relief=GROOVE)
        self.dataDisplayFrame.configure(width=535)

        self.Text1 = Text(self.dataDisplayFrame)
        self.Text1.place(relx=0.04, rely=0.09, relheight=0.82, relwidth=0.42)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(width=226)
        self.Text1.configure(wrap=WORD)

        self.bDone = Button(self.dataDisplayFrame)
        self.bDone.place(relx=0.65, rely=0.7, height=27, width=57)
        self.bDone.configure(activebackground="#d9d9d9")
        self.bDone.configure(text='''Done''')

        self.Label4 = Label(self.dataDisplayFrame)
        self.Label4.place(relx=0.56, rely=0.56, height=19, width=171)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(text='''Done with Attribute values?''')

        self.Label2 = Label(master)
        self.Label2.place(relx=0.37, rely=0.56, height=19, width=126)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''Attributes Preview''')

        self.menubar = Menu(master,bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)

    def onSelect(self,attr):

        # get current id from Listbox
        idx = self.lbAttributes.curselection()
        # get attr name from id
        attrName = self.lbAttributes.get(idx)
        # name the label to this attr
        self.varAttr.set(attrName)

        # Set the variable in text entry to NULL whenever
        # we change selection in Listbox
        self.attrVal.set("")

    def onOkClick(self,event):

        # get current id from Listbox
        idx = self.lbAttributes.curselection()
        # get attr name from id
        attrName = self.lbAttributes.get(idx)

        # get the value of data entered in text entry
        curAttrVal = self.attrValTextBox.get()

        # set curAttrVal in the dictionary we maintain
        self.attrDict[attrName] = [curAttrVal,policy_builder_support.equality.get()]

        # create a list of filled attributes
        listOfFilledAttr = []
        for attr in self.attrList:

            if self.attrDict[attr] not in [None, ["",""]]:
                equality = self.attrDict[attr][1]
                listOfFilledAttr.append(equality.join([attr,self.attrDict[attr][0]]))

        # delete whatever's inside Text1
        self.Text1.delete("1.0",END)

        # populate Text1 using filled attributes' list
        for filledAttr in listOfFilledAttr:
            self.Text1.insert(END,filledAttr+"\n")

if __name__ == '__main__':
    vp_start_gui()
