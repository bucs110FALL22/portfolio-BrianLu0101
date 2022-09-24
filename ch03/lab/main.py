import turtle #1. import modules
import random

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
redSpeed = random.randrange(1,101)
blueSpeed = random.randrange(1,101)
turtle.Screen()

Raphael = turtle.Turtle()
Raphael.shape('turtle')
Raphael.color('red')
Raphael.pu()
Raphael.goto(25,0)
Raphael.lt(90)

Leonardo = turtle.Turtle()
Leonardo.shape('turtle')
Leonardo.color('blue')
Leonardo.pu()
Leonardo.goto(-25,0)
Leonardo.lt(90)

for i in range(10):
    Raphael.fd(redSpeed)
    Leonardo.fd(blueSpeed)

Raphael.goto(25,0)
Leonardo.goto(-25,0)

turtle.exitonclick()

# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode((750,750))

WHITE = (255,255,255)
x = int()
y = int()
coords = [(x,y),(x,y)]
num_sides = [3, 4, 6, 9, 360]
side_length = 100
offset = 500

for i in num_sides:
    window.fill(WHITE)
    for s in range(i):
        theta = (2.0 * math.pi * s) / i
        x = side_length * math.cos(theta) + offset
        y = side_length * math.sin(theta) + offset
        coords.insert(s,(x,y))
        pygame.draw.polygon(window,"black",coords)
        pygame.display.flip()
        pygame.time.wait(125)
        

pygame.quit()

window.exitonclick()
