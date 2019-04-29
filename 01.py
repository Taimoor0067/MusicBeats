#import everything from tkinter
from tkinter import *

#Create Window object
Window=Tk()

#define four labels Title Author year ISBN
l1=Label(Window, text="Title")
l1.grid(row=8,column=8)

l1=Label(Window, text="Author")
l1.grid(row=8,column=2)

l1=Label(Window, text="Year")
l1.grid(row=8,column=8)

l1=Label(Window, text="ISBN")
l1.grid(row=8,column=2)
