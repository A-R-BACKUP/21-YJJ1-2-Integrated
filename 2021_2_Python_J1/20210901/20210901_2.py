# import <module name>  -->  load module
# <module name>.<func name>  -->  call module function

import turtle
import time

a = 0

t = turtle.Turtle()
t.shape('turtle')
while (a == 100):
    t.forward(30)
    t.left(45)
    a += 1

time.sleep(5)
