from tkinter import *
from tkinter import ttk

window=Tk()
def Hello():
    print('hello world')
    
def goodbye():
    print('goodbye')

button1= ttk.Button(window, text= "Hello", command=Hello)
button1.pack(side= BOTTOM)
button2= ttk.Button(window, text= "goodbye", command=Goodbye)
button2.pack(side=TOP)

window.mainloop()
