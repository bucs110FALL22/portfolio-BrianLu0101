import turtle

side = int(input("Number of sides: "))
length = int(input("Length of each side: "))
angle = 360/side

win = turtle.Screen()
Kadrin = turtle.Turtle()
Kadrin.color("red")

for i in range(side):
    for i in range(length):
        Kadrin.fd(length)
    Kadrin.rt(angle)

win.exitonclick()