import pygame
from math import acos, cos, sin
import time

WIDTH, HEIGHT = (800,800)
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("single pendulum")


# constants
FPS = 60
ROPELEN = 300
BALL_MASS = 10  # kg
G = 9.8         # ms^-2
black = (0,0,0)
blue = (0, 138, 255)
white = (255,255,255)
red = (255,23,54)
gray = (130,130,130)
middle_block_pos = (402, 373)



def getangle():
    pos = pygame.mouse.get_pos()

    # avoid division by zero error (kinda shitty)
    if pos[1] == middle_block_pos[1]:
        y_diff = 0.00001 
    else: 
        y_diff = (pos[1] - middle_block_pos[1])
    x_diff = (pos[0] - middle_block_pos[0])


    hyp = ((x_diff ** 2) + (y_diff ** 2)) ** 0.5
    costheta = y_diff / hyp
    theta = acos(costheta)
    if pos[0] < middle_block_pos[0]:
        theta *= -1
    return theta


def getpos():
    pos_theta = getangle()
    coord = [ROPELEN * sin(pos_theta) + middle_block_pos[0], ROPELEN *
cos(pos_theta) + middle_block_pos[1]]
    return coord


init_pos = getpos()
def startsim(coord, g, m):

    return None 





def draw(ball_pos):
    WIN.fill(black)
    pygame.draw.rect(WIN, red, (398, 370, 10, 10))

    # draw the ball and have it be moveable 
    pygame.draw.circle(WIN, blue, (ball_pos[0], ball_pos[1]), 15)

    # draw a line connecting the ball to the square at all times
    pygame.draw.line(WIN, gray, middle_block_pos, (ball_pos[0],
ball_pos[1]))

    pygame.display.update()




def main():
    run = True
    final_pos = False
    start = False
    clock = pygame.time.Clock()


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN :
                final_pos = not final_pos
                start = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and final_pos:
                    start = not start


        if final_pos == False:
            ball_pos = getpos()

        if start:
            #ball_pos = startsim(ball_pos, G, BALL_MASS)
            ball_pos[0] -= 1
            ball_pos[1] += 1



        draw(ball_pos)
        clock.tick(FPS)



main()



