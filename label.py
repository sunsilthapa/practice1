from tkinter import *

root=Tk()

#creation of a label widget and placing them onto the screen based on x and y coordinates
myLabe1=Label(root, text="hello tkinter").grid(row=0,column=0)
myLabel2=Label(root, text="hello 31 A").grid(row=0, column=0)
myLabel3=Label(root, text="hello 31 B").grid(row=1,cloumn=1)

root.mainloop()