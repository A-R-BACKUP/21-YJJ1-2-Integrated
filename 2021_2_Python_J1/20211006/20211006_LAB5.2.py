#LAB 5-2 + Challenge 5.4

import turtle
t = turtle.Turtle()

for triangle in range(3):
    t.forward(100)
    t.left(360/3)

t.penup()
t.goto(200, 0)
t.pendown()

for rectangle in range(4):
    t.forward(100)
    t.left(360/4)

# Challenge 5.4: Draw hexagon

t.penup()
t.goto(-300, 0)
t.pendown()

for hexagon in range(6):
    t.forward(50)
    t.left(360/6)