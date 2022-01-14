'''
#Creation an icon
from tkinter import *
#from tkinter inport image
root=Tk()

#title
root.title('Images Insertion')

#icons image
#png icons does not support sometimes
root.iconbitmap('C:\Users\Sandip thap\Desktop\tkinter\iconimage.py')

root.mainloop()'''

from tkinter import *
from PIL import ImageTk, Image  #importing python image library
root=Tk()
#title
root.title('Images Insertion')

#icon images
#png images does not support sometimes
root.iconbtimap('C:\Users\Sandip thapa\Documents\programming and algorithms\tkinter work\images')

my_image=ImageTk.