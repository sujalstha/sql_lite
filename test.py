import turtle
from turtle import *

# SCREEN SETUP

setup(800, 500)
title("Turtle Race")
bgcolor("forestgreen")
speed(0)

# HEADING
penup()
goto(-100, 205)
color("white")
write("TURTLE RACE", font=("Arial", 20, "bold"))

# Track
goto(-350, 200)
pendown()
color("chocolate")
begin_fill()

for i in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()

# FINISH LINE
gap_size = 20
shape("square")
penup()

# WHITE SQUARES ROW 1
color("white")

for i in range(10):
    goto(250, (170 - (i * gap_size * 2)))
    stamp()

# WHITE SQUARES ROW 2
for i in range(10):
    goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
    stamp()

mainloop()
