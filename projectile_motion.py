import pygame
from math import sin, cos
pygame.init()

#Set Up
window = pygame.display.set_mode((1200,750))
pygame.display.set_caption("Projectile Motion")
run = True
clock = pygame.time.Clock()

#Constants
ball_x = 10.0
ball_y = 730.0
ball_v_x = 45.0 * cos(125)
ball_v_y = 45.0 * sin(125) 
ball_a_x = 0.0 
ball_a_y = 9.8
theta = None 
time = 1.0 


def draw_ball(x,y):
    pygame.draw.circle(window, (0,138,255), (x,y), 15)
    return None



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #window.fill((0,0,0))
    draw_ball(ball_x, ball_y)
    ball_x = ball_x + (ball_v_x * time) + 0.5 * (ball_a_x * (time)**2)
    ball_y = ball_y + (ball_v_y * time) + 0.5 * (ball_a_y * (time)**2)
    
    clock.tick(60)
    time += 1.0
    pygame.display.update()



