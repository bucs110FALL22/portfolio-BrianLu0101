import turtle
win = turtle.Screen()
Numas = turtle.Turtle()

Numas.shape('turtle')
Numas.color('purple')

for a in range(4):
    Numas.fd(50)
    Numas.rt(90)

Numas.color('red')
Numas.pu()
Numas.fd(300)
Numas.pd()
Numas.lt(90)

for b in range(4):
    Numas.fd(75)
    Numas.lt(90)

win.exitonclick()