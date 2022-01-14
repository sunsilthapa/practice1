from tkinter import *
root=Tk()
#creation of a button widget
redButton=Button(root, text='Left', fg='green')
#packing it in the screen for showing
redButton.pack(side=LEFT)

greenButton=Button(root, text='Right', fg='green')
greenButton.pack(side=RIGHT)

blackButton=Button(root, text='Button', fg='black')
blackButton.pack(side=BOTTOM)

blueButton=Button(root, text='Top', fg='blue')
blueButton.pack(side=TOP)

root.mainloop()


