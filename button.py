from tkinter import *
root=Tk()
#creation of a button widget
myButton1=Button(root, text="Click Me")
myButton1.pack()

#creaton of a disabled button widget
myButton2=Button(root, text="Click Me" ,state=DISABLED)
myButton2.pack()

#button with x and y co-ordinates
myButton3=Button(root, text="Click Me", pady=50)
myButton3.pack()

myButton4=Button(root, text="Click Me",padx=50, pady=50)
myButton4.pack()

root.mainloop()
