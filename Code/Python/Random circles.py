from tkinter import *
from random import *

size = 500
window = Tk()
c = Canvas(window, width=size, height=size)
c.pack()

while True:
    col = choice(["red", "green", "blue", "black"])
    x0 = uniform(0, size)
    y0 = uniform(0, size)
    col_random = choice(col)
    d = uniform(0, size/5)
    c.create_oval(x0, y0, x0+d, y0+d, fill=col)
    window.update()  


