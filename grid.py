#grid() method
from tkinter import *
root=Tk()
#alignning the labels and contents in row and column
name=Label(root,text="Name").grid(row=0,column=0)
e1=Entry(root).grid(row=0,column=1)

password=Label(root, text="Password").grid(row=1, column=0)
e2=Entry(root).grid(row=1,column=1)

submitButton=Button(root, text="Submit").grid(row=4,column=1)

root.mainloop()

