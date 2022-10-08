import pygame
import random
import math


pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill('black')

pygame.draw.circle(screen, 'green', (250,250), 250)
pygame.draw.line(screen, 'black', (0,250), (500, 250))
pygame.draw.line(screen, 'black', (250,0), (250, 500))
pygame.display.flip()

for i in range(10):
    x = random.randrange(0,500)
    y = random.randrange(0,500)
    distance_from_center = math.hypot(x-250,y-250)
    is_in_circle = distance_from_center <= 500/2

    if is_in_circle:
        pygame.draw.circle(screen, 'black', (x,y), 10)
    else:
        pygame.draw.circle(screen, 'white', (x,y), 10)
    
    pygame.display.flip()
    pygame.time.delay(500)

screen.fill('black')
pygame.draw.rect(screen, 'red', (10, 10, 50, 50))
pygame.draw.rect(screen, 'blue', (440, 10, 50, 50))
pygame.display.flip()

print('Red or Blue?')
guess = ''
op = True
while op:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos >= (10,10) and event.pos <= (60,60):
            guess = 'Red'
            print('You chose Red')
            op = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos >= (440,10) and event.pos <= (490,60):
            guess = 'Blue'
            print('You chose Blue')
            op = False

screen.fill('black')
pygame.draw.circle(screen, 'green', (250, 250), 250)
pygame.draw.line(screen, 'black', (0, 250), (500, 250))
pygame.draw.line(screen, 'black', (250, 0), (250, 500))
pygame.display.flip()

p1pts = 0
p2pts = 0
round = 1

for i in range(10):
    x = random.randrange(0, 500)
    y = random.randrange(0, 500)
    x1 = random.randrange(0, 500)
    y1 = random.randrange(0, 500)

    distance_from_center = math.hypot(x - 250, y - 250)
    is_in_circle = distance_from_center <= 500 / 2
    distance_from_center1 = math.hypot(x1 - 250, y1 - 250)
    is_in_circle1 = distance_from_center1 <= 500 / 2

    print('Round', round)
    pygame.time.delay(500)

    if is_in_circle:
        pygame.draw.circle(screen, 'red', (x, y), 10)
        p1pts += 1
        print('red hit')
    else:
        pygame.draw.circle(screen, 'white', (x, y), 10)
        print('red miss')

    pygame.display.flip()
    pygame.time.delay(500)

    if is_in_circle1:
        pygame.draw.circle(screen, 'blue', (x1, y1), 10)
        p2pts += 1
        print('blue hit')
    else:
        pygame.draw.circle(screen, 'white', (x1, y1), 10)
        print('blue miss')
    pygame.display.flip()
    pygame.time.delay(500)
    round = round + 1

victorR = p1pts > p2pts
victorB = p1pts < p2pts
tiehold = p1pts == p2pts

if victorR:
    print('Winner: RED (', p1pts, ')')
    if guess.lower() == 'red':
        print('You guessed correctly.')
    else:
        print('You guessed incorrectly. (', p2pts, ')')
elif victorB:
    print('Winner: BLUE (', p2pts, ')')
    if guess.lower() == 'blue':
        print('You guessed correctly.')
    else:
        print('You guessed incorrectly. (', p1pts, ')')
else:
    print('Tie')

pygame.quit()
