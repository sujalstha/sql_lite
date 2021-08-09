from turtle import *
import time
from random import *

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

# BLACK SQUARES ROW 1
color("black")
for i in range(10):
    goto(250, (190 - (i * gap_size * 2)))
    stamp()

# BLACK SQUARES ROW 2
for i in range(10):
    goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
    stamp()

# TURTLE 1 - BLUE
blue_turtle = Turtle()
blue_turtle.color("cyan")
blue_turtle.shape("turtle")
blue_turtle.shapesize(1.5)
blue_turtle.penup()
blue_turtle.goto(-300, 150)

# TURTLE 2 - PINK
pink_turtle = Turtle()
pink_turtle.color("magenta")
pink_turtle.shape("turtle")
pink_turtle.shapesize(1.5)
pink_turtle.penup()
pink_turtle.goto(-300, 50)

# TURTLE 3 - YELLOW
yellow_turtle = Turtle()
yellow_turtle.color("yellow")
yellow_turtle.shape("turtle")
yellow_turtle.shapesize(1.5)
yellow_turtle.penup()
yellow_turtle.goto(-300, -50)

# TURTLE 4 - GREEN
green_turtle = Turtle()
green_turtle.color("lime")
green_turtle.shape("turtle")
green_turtle.shapesize(1.5)
green_turtle.penup()
green_turtle.goto(-300, -150)

# PAUSE FOR 5 SECOND BEFORE RACING
time.sleep(1)

color("black")
shape("arrow")

while blue_turtle.xcor() <= 230 and pink_turtle.xcor() <= 230 and \
        yellow_turtle.xcor() <= 230 and green_turtle.xcor() <= 230:
    blue_turtle.forward(randint(0, 11))
    pink_turtle.forward(randint(0, 11))
    yellow_turtle.forward(randint(0, 11))
    green_turtle.forward(randint(0, 11))

    if blue_turtle.xcor() >= 230:
        goto(-100, 0)
        pendown()
        color("white")
        write("Blue Won!", font=("Arial", 20, "bold"))
        color("chocolate")

    elif pink_turtle.xcor() >= 230:
        goto(-100, 0)
        pendown()
        color("white")
        write("Pink Won!", font=("Arial", 20, "bold"))
        color("chocolate")
    elif yellow_turtle.xcor() >= 230:
        goto(-100, 0)
        pendown()
        color("white")
        write("Yellow Won!", font=("Arial", 20, "bold"))
        color("chocolate")

mainloop()
