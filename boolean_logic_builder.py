#! /usr/bin/env python
# GUI was generated using PAGE v4.5 in conjuction with Tcl v8.6

from Tkinter import *

import os
import sys
import ttk

import policy_builder
import boolean_logic_builder_support

def vp_start_gui():
	'''Starting point when module is the main routine.'''
	global val, w, root
	root = Tk()
	root.title('New_Toplevel_1')
	geom = "600x608+434+86"
	root.geometry(geom)
	w = New_Toplevel_1 (root)
	boolean_logic_builder_support.init(root, w)
	root.mainloop()

w = None
def create_New_Toplevel_1(root, param=None):
	'''Starting point when module is imported by another program.'''
	global w, w_win, rt
	rt = root
	w = Toplevel (root)
	w.title('New_Toplevel_1')
	geom = "600x608+434+86"
	w.geometry(geom)
	w_win = New_Toplevel_1 (w)
	boolean_logic_builder_support.init(w, w_win, param)
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

		self.attrFile = open("list_of_attr","r")
		# Read and map attributes to a list
		self.listOfAttributes = map(str,self.attrFile.read().split("\n"))
		# Filter empty attributes
		self.listOfAttributes = filter(None,self.listOfAttributes)
		self.attrFile.close()
		os.remove("list_of_attr")

		self.listOfAttributesFinal = []
		for attr in self.listOfAttributes:
			curr_key = map(str,attr.split())
			curr_key = curr_key[0].replace("_"," ")
			if policy_builder.attrTypeMap[curr_key] == "String":
				tmpAttr = attr.replace(" = ", "__")
				self.listOfAttributesFinal.append(tmpAttr)
			elif policy_builder.attrTypeMap[curr_key] == "Date":
				tmpAttr = attr.replace("/", "")
				self.listOfAttributesFinal.append(tmpAttr)
			else:
				self.listOfAttributesFinal.append(attr)


		self.booleanExpressionFinal = []
		self.booleanExpressionFinalString = ""

		self.Frame1 = Frame(master)
		self.Frame1.place(relx=0.05, rely=0.05, relheight=0.55, relwidth=0.89)
		self.Frame1.configure(relief=GROOVE)
		self.Frame1.configure(borderwidth="1")
		self.Frame1.configure(relief=GROOVE)
		self.Frame1.configure(background="#e5e5e5")
		self.Frame1.configure(width=535)

		self.lbAttributes = Listbox(self.Frame1)
		self.lbAttributes.place(relx=0.04, rely=0.09, relheight=0.73, relwidth=0.42)
		self.lbAttributes.configure(background="white")
		self.lbAttributes.configure(borderwidth="0")
		self.lbAttributes.configure(font="TkFixedFont")
		self.lbAttributes.configure(selectbackground="#c4c4c4")

		for idx in xrange(len(self.listOfAttributes)):
			self.lbAttributes.insert(END,chr(ord('a')+idx) + " : " + self.listOfAttributes[idx])

		self.lbAttributes.select_set(0) #This only sets focus on the first item.
		self.lbAttributes.event_generate("<<ListboxSelect>>")

		vcmd = (master.register(self.validate),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		self.entryBooleanLogic = Entry(self.Frame1, validate = 'key', validatecommand = vcmd)
		self.entryBooleanLogic.place(relx=0.5, rely=0.15, relheight=0.18, relwidth=0.44)
		self.entryBooleanLogic.configure(background="white")
		self.entryBooleanLogic.configure(font="TkFixedFont")
		self.entryBooleanLogic.configure(selectbackground="#c4c4c4")
		self.entryBooleanLogic.configure(disabledbackground="#f9f9f9")


		self.Label1 = Label(self.Frame1)
		self.Label1.place(relx=0.56, rely=0.09, height=19, width=176)
		self.Label1.configure(activebackground="#f9f9f9")
		self.Label1.configure(text='''Boolean Logic Textbox''')

		self.bOK = Button(self.Frame1)
		self.bOK.place(relx=0.65, rely=0.75, height=27, width=62)
		self.bOK.configure(activebackground="#d9d9d9")
		self.bOK.configure(text='''Ok''')
		self.bOK.bind("<Button-1>",self.onOKClick)

		self.Label3 = Label(self.Frame1)
		self.Label3.place(relx=0.04, rely=0.03, height=19, width=224)
		self.Label3.configure(activebackground="#f9f9f9")
		self.Label3.configure(text='''Attributes and Values''')
		self.Label3.configure(width=224)

		self.bInsert = Button(self.Frame1)
		self.bInsert.place(relx=0.17, rely=0.87, height=27, width=61)
		self.bInsert.configure(activebackground="#d9d9d9")
		self.bInsert.configure(text='''Insert''')
		self.bInsert.bind("<Button-1>",self.onInsertClick)

		self.bOpenParen = Button(self.Frame1)
		self.bOpenParen.place(relx=0.52, rely=0.39, height=27, width=31)
		self.bOpenParen.configure(activebackground="#d9d9d9")
		self.bOpenParen.configure(text='''(''')
		self.bOpenParen.bind("<Button-1>",self.onOpenParenClick)

		self.bCloseParen = Button(self.Frame1)
		self.bCloseParen.place(relx=0.62, rely=0.39, height=27, width=31)
		self.bCloseParen.configure(activebackground="#d9d9d9")
		self.bCloseParen.configure(text=''')''')
		self.bCloseParen.bind("<Button-1>",self.onCloseParenClick)

		self.bAND = Button(self.Frame1)
		self.bAND.place(relx=0.71, rely=0.39, height=27, width=52)
		self.bAND.configure(activebackground="#d9d9d9")
		self.bAND.configure(text='''AND''')
		self.bAND.bind("<Button-1>",self.onANDClick)

		self.bOR = Button(self.Frame1)
		self.bOR.place(relx=0.84, rely=0.39, height=27, width=43)
		self.bOR.configure(activebackground="#d9d9d9")
		self.bOR.configure(text='''OR''')
		self.bOR.bind("<Button-1>",self.onORClick)

		self.Message1 = Message(self.Frame1)
		self.Message1.place(relx=0.47, rely=0.51, relheight=0.19, relwidth=0.51)
		self.Message1.configure(justify=CENTER)
		self.Message1.configure(text='''Select the attribute from left and click Insert. Use the above buttons to form a proper Boolean Expression. Click OK once done.''')
		self.Message1.configure(width=275)
		self.Message1.configure(background="#e5e5e5")

		self.Frame2 = Frame(master)
		self.Frame2.place(relx=0.05, rely=0.67, relheight=0.29, relwidth=0.89)
		self.Frame2.configure(relief=GROOVE)
		self.Frame2.configure(borderwidth="2")
		self.Frame2.configure(relief=GROOVE)
		self.Frame2.configure(width=535)

		self.textBooleanExpressionPreview = Text(self.Frame2)
		self.textBooleanExpressionPreview.place(relx=0.04, rely=0.11, relheight=0.38, relwidth=0.93)
		self.textBooleanExpressionPreview.configure(background="white")
		self.textBooleanExpressionPreview.configure(font="TkTextFont")
		self.textBooleanExpressionPreview.configure(selectbackground="#c4c4c4")
		self.textBooleanExpressionPreview.configure(width=496)
		self.textBooleanExpressionPreview.configure(wrap=WORD)
		self.textBooleanExpressionPreview.configure(state=DISABLED)

		self.bDone = Button(self.Frame2)
		self.bDone.place(relx=0.45, rely=0.74, height=27, width=57)
		self.bDone.configure(activebackground="#d9d9d9")
		self.bDone.configure(text='''Done''')
		self.bDone.bind("<Button-1>",self.onDoneClick)

		self.Label4 = Label(self.Frame2)
		self.Label4.place(relx=0.28, rely=0.57, height=19, width=232)
		self.Label4.configure(activebackground="#f9f9f9")
		self.Label4.configure(text='''Click Done if the above preview is fine''')

		self.Label2 = Label(master)
		self.Label2.place(relx=0.35, rely=0.63, height=19, width=176)
		self.Label2.configure(activebackground="#f9f9f9")
		self.Label2.configure(text='''Boolean Logic Preview''')

		self.menubar = Menu(master,bg=_bgcolor,fg=_fgcolor)
		master.configure(menu = self.menubar)


	def validate(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):

		# Add allowed characters in validString
		validString = []
		for attr in self.lbAttributes.get(0,END):
			validString.append(attr[0])
		validString.append("( ")
		validString.append("(")
		validString.append(" )")
		validString.append(")")
		validString.append(" & ")
		validString.append("&")
		validString.append(" | ")
		validString.append("|")
		validString.append(" ")

		if text in validString:
			return True
		else:
			return False


	def onInsertClick(self, event):

		# get current id from Listbox
		idx = self.lbAttributes.curselection()
		# get first character of attr name from id
		attrNameMap = self.lbAttributes.get(idx)[0]

		self.entryBooleanLogic.insert(INSERT,attrNameMap)

	def onOpenParenClick(self, event):

		self.entryBooleanLogic.insert(INSERT,"( ")

	def onCloseParenClick(self, event):

		self.entryBooleanLogic.insert(INSERT," )")

	def onANDClick(self, event):

		self.entryBooleanLogic.insert(INSERT," & ")

	def onORClick(self, event):

		self.entryBooleanLogic.insert(INSERT," | ")

	def onOKClick(self, event):

		# Better is only for display purpose
		# Final is used to print to the file
		booleanExpression = self.entryBooleanLogic.get()
		booleanExpressionBetter = []
		self.booleanExpressionFinal = []
		for i in booleanExpression:
			if i >= 'a' and i <= 'z':
				booleanExpressionBetter.append(self.listOfAttributes[ord(i)-ord('a')])
				self.booleanExpressionFinal.append(self.listOfAttributesFinal[ord(i)-ord('a')])
			else:
				if i == "&":
					booleanExpressionBetter.append("AND")
					self.booleanExpressionFinal.append("and")
				elif i == '|':
					booleanExpressionBetter.append("OR")
					self.booleanExpressionFinal.append("or")
				else:
					booleanExpressionBetter.append(i)
					self.booleanExpressionFinal.append(i)

		booleanExpressionBetterString = ''.join(booleanExpressionBetter)
		self.booleanExpressionFinalString = ''.join(self.booleanExpressionFinal)

		self.textBooleanExpressionPreview.configure(state=NORMAL)
		self.textBooleanExpressionPreview.delete(1.0,END)
		self.textBooleanExpressionPreview.insert(END,booleanExpressionBetterString)
		self.textBooleanExpressionPreview.configure(state=DISABLED)

	def onDoneClick(self, event):

		# write final boolean expression in text file
		tmp_txt_file = open("policy_file","w")
		tmp_txt_file.write("%s\n" % self.booleanExpressionFinalString)
		tmp_txt_file.close()
		destroy_New_Toplevel_1()

