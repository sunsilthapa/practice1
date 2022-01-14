#button with event
'''from tkinter import *

root=Tk()

def myClick():
    myLabel=Label(root, text="Button is clicked")
    myLabel.pack()
#creation of a button widget and adding clicklistener to it
myButton1=Button(root, text="Click Me", command=myClick)
myButton1.pack()

root.mainloop()'''

#button with color
'''from tkinter import *
root=Tk()
def myClick():
    myLabel=Label(root, text="botton is clicked")
    myLabel.pack()
#creation of a button widget and adding clicklistener to it
myButton1=Button(root, text="Click me", command=myClick, fg="white", bg="grey")
myButton1.pack()
root.mainloop()'''

#creting input fields(Entry)
from tkinter import *
root=Tk()

e1=Entry(root, width=50, fg="blue",bg="white", borderwidth=5)
e1.pack()

def myClick():
    myLabel1=Label(root, text="Button is clicked")
    myLabel1.pack()
myButton1=Button(root, text="Click Me", command=myClick)
myButton1.pack()
root.mainloop()