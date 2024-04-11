from tkinter import *
from tkinter.simpledialog import askinteger, askfloat, askstring
from tkinter.filedialog import (askopenfile, asksaveasfile, askopenfiles,
                                askopenfilename,asksaveasfilename,askopenfilenames,
                                askdirectory)
from tkinter.colorchooser import askcolor
from tkinter import ttk

from tkinter import messagebox

gui = Tk()
gui.geometry("300x200")

# def inp():
#     #num = askstring("input","Enter an string:")
#     filename = askopenfilenames()
#     print(filename)
#
#     color = askcolor()
#     print(color)

b = Button(gui, text="Click Here", command=inp)
b.place(x=50, y=50)

frame = Frame(gui)
frame.pack()
animals = ['Cow', 'Dog', 'Lion', 'Monkey', 'Giraffe']
combo = ttk.Combobox(frame, values=animals)
combo.set('Select an animal')
combo.pack(padx=5, pady=5)
gui.mainloop()

frame = Frame(gui)



