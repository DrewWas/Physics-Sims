import pygame
from time import time
from math import cos, sin, atan2, degrees, pi

WIDTH, HEIGHT = (800, 800)
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pendulum")

# we increase G in order to increase the period, thus making the pendulum swing faster
G = 9.81 * 500
mass = 1
black = (0,0,0)
gray = (128,128,128)
# blue ball is small angle approximation
blue = (0,138,255)
# pink ball is solved using the non-linear DEq
pink = (255, 41, 255)
red = (255, 23, 54)
block_x = (WIDTH // 2) - 20
block_y = (HEIGHT// 2) - 125
gameStart = False
dt = 0.01

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            gameStart = not gameStart
            start_time = time()
            blue_ball_pos = list(init_pos)
            pink_ball_pos = list(init_pos)

            #
            x_diff =  blue_ball_pos[0] - (block_x + 4)
            y_diff =  blue_ball_pos[1] - (block_y + 4)
            rope_len = ((x_diff ** 2) + (y_diff ** 2)) ** 0.5
            period = 2 * pi * ((rope_len / G) ** 0.5)
            angle_rad = atan2(x_diff, y_diff)
            #


    win.fill(black)

    #Draw a single block to the screen (anchor point)
    pygame.draw.rect(win, red, (block_x, block_y, 10, 10))

    if not gameStart:
        init_pos = pygame.mouse.get_pos()
        pygame.draw.circle(win, blue, (init_pos), 20)

    if gameStart:
        pygame.draw.circle(win, blue, (blue_ball_pos), 20)
        pygame.draw.line(win, gray, (block_x + 4, block_y + 4), (blue_ball_pos))

        # get elapsed time
        elap_time = time() - start_time
        theta = angle_rad * cos(elap_time * ((G / rope_len) ** 0.5))        
        real_theta = solve_ODE(theta)
        
        blue_ball_pos[0] = block_x + 4 + rope_len * sin(theta)
        blue_ball_pos[1] = block_y + 4 + rope_len * cos(theta)
        pink_ball_pos[0] = block_x + 4 + rope_len * sin(real_theta)
        pink_ball_pos[1] = block_y + 4 + rope_len * cos(real_theta)

    pygame.display.update()






