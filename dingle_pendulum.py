import pygame
from time import time
from math import cos, sin, atan2, degrees

WIDTH, HEIGHT = (800, 800)
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pendulum")

black = (0,0,0)
gray = (128,128,128)
blue = (0,138,255)
red = (255, 23, 54)
block_x = (WIDTH // 2) - 20
block_y = (HEIGHT// 2) - 125
gameStart = False

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            gameStart = not gameStart
            start_time = time()
            ball_pos = list(init_pos)

    win.fill(black)

    #Draw a single block to the screen (anchor point)
    pygame.draw.rect(win, red, (block_x, block_y, 10, 10))


    if not gameStart:
        init_pos = pygame.mouse.get_pos()
        pygame.draw.circle(win, blue, (init_pos), 20)

    if gameStart:
        pygame.draw.circle(win, blue, (ball_pos), 20)
        pygame.draw.line(win, gray, (block_x + 4, block_y + 4), (ball_pos))

        # get angle
        x_diff =  ball_pos[0] - (block_x + 4)
        y_diff =  ball_pos[1] - (block_y + 4)
        angle_rad = atan2(x_diff, y_diff)    # which do we use???
        angle_deg = degrees(angle_rad)       # which do we use???

        # get elapsed time
        elap_time = time() - start_time
        print(elap_time)


    pygame.display.update()


"""
PLAN:

* Draw a single block to the screen (anchor point) *************

* Draw a ball to the screen with variable x and y coords ************

* The ball is moveable by the mouse until a click      *************
	- After the click, the x and y coords are locked  **************

* The x and y coords of the ball are updateable     ************

* Do the math on forces (even tho some may not be visually present)
	- Get angle    *******
	- Get elapsed time
	- Get forces
	- Apply forces



* Attach string

"""




