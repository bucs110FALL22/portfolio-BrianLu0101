import turtle
import random

turtle.Screen()
turtle.setup(500,500)
Rogul = turtle.Turtle()
Rogul.lt(90)

while True:
    coin = random.randint(1,2)
    a = 250
    b = -250
    if Rogul.xcor() > a or Rogul.xcor() < b or Rogul.ycor() > a or Rogul.ycor() < b:
        break
    elif coin == 1:
        print('Heads')
        Rogul.lt(90)
    elif coin == 2:
        print("Tails")
        Rogul.rt(90)
    Rogul.fd(50)

Rogul.pu()
Rogul.goto(0,0)

turtle.exitonclick()
