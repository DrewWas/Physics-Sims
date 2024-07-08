import pygame
from random import randint

# Setup
pygame.init()

WIDTH = 1400
HEIGHT = 800
BLUE = (0,138,255)
BLACK = (0,0,0)
FPS = 120
RADIUS = 10
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('balls')


class Balls:

    def __init__(self):
        self.x_pos = randint(200, 1200)
        self.y_pos = randint(0, 200) 
        #self.x_vel = randint(-3, 3) 
        self.x_vel = 0 
        self.y_vel = 0 
        self.x_acc = 0  
        self.y_acc = 9.8 / 50    # Divide by 250 to normalize 


    def draw(self):
        self.y_pos += self.y_vel
        self.y_vel += self.y_acc
        
        self.x_pos += self.x_vel
        self.x_vel += self.x_acc

        pygame.draw.circle(SCREEN, BLUE, (self.x_pos, self.y_pos), RADIUS)

        if self.y_pos >= HEIGHT - (RADIUS * 1.1):
            self.y_pos = HEIGHT - (RADIUS * 1.1) - 1 
            self.y_vel *= -(1/2)
            print(self.y_vel)
            
            if abs(self.y_vel) < 1:
                self.y_acc = 0        
                self.y_vel= 0        





def main():

    running = True
    clock = pygame.time.Clock()
    balls = [Balls() for i in range(10)]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        SCREEN.fill(BLACK)
        for ball in balls:
            ball.draw()


        pygame.display.flip()  

    pygame.quit()


main()





