import pygame
import math
pygame.init()

window = pygame.display.set_mode((700,700))
pygame.display.set_caption("Bounce Fr")
clock = pygame.time.Clock()

blue = (0, 138, 255)
black = (0, 0, 0)

class Ball:
    def __init__(self, ball_x, ball_y, x_velo, y_velo):
        self.x = ball_x
        self.y = ball_y
        self.vx = x_velo
        self.vy = y_velo


    def draw(self):
        window.fill(black)
        pygame.draw.circle(window, blue, (self.x, self.y), 15)

        
    def update(self):
        self.y += 9.8 * elap
        pygame.display.update()

def main():
    run = True
    yuh = Ball(100,100,0,0)
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        yuh.draw()
        yuh.update()
        clock.tick(60)

main()




