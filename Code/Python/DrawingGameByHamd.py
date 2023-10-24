from turtle import *


setup(800,600)
home()
pen_size = 10
color("black")
title("Drawing Board")
speed("fastest") 
drawdist= 10 
current_state = penup
next_state = pendown

#Button Instructions
def move_up():
        seth(90)
        forward(drawdist)

def move_down():
        seth(270)
        forward(drawdist)

def move_left():
        seth(180)
        forward(drawdist)

def move_right():
        seth(0)
        forward(drawdist)


def space_bar():
    global current_state, next_state
    next_state()
    current_state, next_state = next_state, current_state

#Change Pen Color
def red():
        color("red")

def green():
        color("green")

def blue():
        color("blue")
def orange():
        color('orange')
def yellow():
        color('yellow')
def purple():
        color('purple')
def black():
        color('black')
def erase():
        color('white')
        
#Button Triggers
s= getscreen()

s.onkey(move_up,"Up")

s.onkey(move_down,"Down")

s.onkey(move_left,"Left")

s.onkey(move_right,"Right")

s.onkey(space_bar,"space")

s.onkey(red,"r")

s.onkey(green,"g")

s.onkey(blue,"b")

s.onkey(orange,'o')

s.onkey(yellow, 'y')

s.onkey(purple, 'p')

s.onkey(black, 'b')

s.onkey(erase, 'e')

listen()

done()
