import pygame

pygame.init()
window = pygame.display.set_mode((500,500))
window.fill('white')
pygame.display.flip()
window2 = pygame.transform.flip(window, False, True)
font = pygame.font.Font(None, 50)
n = 101
count = 0
start = 2
upper_limit = 20
iters = {}
max_so_far = 0
max_val = 0
scale = 5

while n != 1:
    if (n % 2) == 0:
        n = n/2
        count += 1
        print(n)
    else:
        n = 3 * n + 1
        count += 1
        print(n)

print(count)


for i in range(start, upper_limit + 1):
    n = i
    count = 0
    while n != 1:
        if (n % 2) == 0:
            n = n/2
        else:
            n = 3 * n + 1
            count += 1
        iters[i] = count

print(iters)

for i in range(2, upper_limit):
    count = 0
    n = i
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
            count += 1
        iters[i] = count
        coordinates = list(iters.items())
        pygame.draw.lines(window, 'black', False, coordinates * scale)
        pygame.display.flip()
        if max_so_far < count:
            max_so_far = count
            max_val = max_so_far
    pygame.time.delay(500)

msg = font.render(str(max_so_far),True,'blue')
window.blit(msg, (15,15))