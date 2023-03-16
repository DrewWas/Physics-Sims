import pygame
import math
pygame.init()

window = pygame.display.set_mode((700,700))
pygame.display.set_caption("Bounce Fr")
run = True
clock = pygame.time.Clock()

class Ball:
    def __init__(self, ball_x, ball_y, x_velo, y_velo):
        self.x = ball_x
        self.y = ball_y
        self.vx = x_velo
        self.vy = y_velo
   
    def update(self):
        
        


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(60)
    Ball.draw 
    pygame.display.update()
