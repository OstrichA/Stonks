from tkinter import *
window = Tk()
def Baction():
    print("Hi")
buttonA=Button(window, text="pfefferpotthast", command=Baction)
buttonA.pack()
window.mainloop()