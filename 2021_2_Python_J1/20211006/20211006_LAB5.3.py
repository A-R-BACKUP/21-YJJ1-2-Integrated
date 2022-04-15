#LAB 5-3 + Challenge 5.5


import turtle
t = turtle.Turtle()

s = turtle.textinput("", "몇각형을 그릴까요?: ")
n = int(s)

f = turtle.textinput("", "한변의 길이를 입력하세요:")
q = int(f)

for i in range(n):
    t.forward(q)
    t.left(360/n)