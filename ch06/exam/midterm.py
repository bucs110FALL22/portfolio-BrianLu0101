import turtle
import random

turtle1 = turtle.Turtle()

xmeteor = [-250, 100, -175 ,-300, 50, 300]
ymeteor = [-300, -250, 100, 300, -75, 300]

streaksx = [10, -10, -25]
streaksy = [10, 45, 70]
streakex = [100, 110, 125]
streakey = [100, 145, 170]

streakcol = ['red', 'orange', 'yellow']



def main():
    screen = turtle.Screen()
    screen.bgcolor('black')    

    turtle1.speed(10)

    turtle1.lt(90)

    stars()
    meteor(xmeteor,ymeteor,streaksx,streaksy,streakex,streakey,streakcol)

    screen.exitonclick()



def meteor(x,y,distsx,distsy,distex,distey,color):
    i = 0
    o = 0

    while i <= len(x)-1 and o <= len(y)-1:
        turtle1.pu()
        turtle1.goto(x[i],y[i])
        turtle1.pd()
        turtle1.pencolor('brown')
        turtle1.fillcolor('brown')
        turtle1.begin_fill()
        turtle1.circle(50)
        turtle1.end_fill()

        q = 0
        r = 0
        l = 0
        p = 0
        k = 0

        while q <= len(distsx)-1 and r <= len(distsy)-1 and l <= len(distex) and p <= len(distey) and k <= len(color):
            turtle1.pu()
            turtle1.goto(x[i]+distsx[q],y[o]+distsy[r])
            turtle1.pd()
            turtle1.pencolor(color[k])
            turtle1.goto(x[i]+distex[l],y[o]+distey[p])

            q += 1
            r += 1
            l += 1
            p += 1
            k += 1

        i += 1
        o += 1



def stars():
    for i in range(50):
        xstar = random.randrange(-450,450)
        ystar = random.randrange(-450,450)
        
        turtle1.pu()
        turtle1.goto(xstar,ystar)
        turtle1.pd()
        turtle1.dot(5, 'white')



main()