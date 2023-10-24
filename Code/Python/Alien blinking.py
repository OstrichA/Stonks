from tkinter import*
window=Tk()
window.title("Alien")
c=Canvas(window, height=300, width=400)
c.pack()
body=c.create_oval(100, 150, 300, 250, fill="green")
eye=c.create_oval(170, 70, 230, 130, fill="white")
eyeball=c.create_oval(190, 90, 210, 110, fill="black")
mouth=c.create_oval(150, 220, 250, 240, fill="red")
neck=c.create_line(200, 150, 200, 130)
hat=c.create_polygon(180, 75, 220, 75, 200, 20, fill="blue")

def mouth_open(event):
    c.itemconfig(mouth, fill="black")
c.bind_all("<Button-1>", mouth_open)
def mouth_close(event):
    c.itemconfig(mouth, fill="red")
c.bind_all("<Button-3>", mouth_close)
def blink(event):
    c.itemconfig(eye, fill="green")
    c.itemconfig(eyeball, state=HIDDEN)
c.bind_all("<Button-5>", blink)
def unblink(event):
    c.itemconfig(eye, fill="white")
    c.itemconfig(eyeball, state=NORMAL)
c.bind_all("<Button-4>", unblink)
words=c.create_text(200, 280, text="I am an alien")
def steal_hat(event):
    c.itemconfig(hat, state=HIDDEN)
    c.itemconfig(words, text="Give my hat back")
c.bind_all("<Button-2>", steal_hat)

def eye_control(event):
    key = event.keysym
    if key == "Up":
        c.move(eyeball, 0, -5)
    elif key == "Down":
        c.move(eyeball, 0, 5)    
    elif key == "Left":
        c.move(eyeball, -5, 0)
    elif key == "Right":
        c.move(eyeball, 5, 0)
c.bind_all("<Key>", eye_control)

mainloop()