import pygame
from math import sin, cos
pygame.init()

#Set Up
window = pygame.display.set_mode((1200,750))
pygame.display.set_caption("Projectile Motion")
run = True
clock = pygame.time.Clock()


class Canon:
    g = -9.81
    def __init__(self, angle, magnitude):
        self.angle = angle
        self.magnitude = magnitude

        self.x_pos = 0
        self.y_pos = 0

        self.x_velo = 0
        self.y_velo = 0

        self.y_acc = self.g 


    def launch(self,time):
        def ball_x_pos(time):
            self.x_velo = self.magnitude * cos(self.angle)
            self.x_pos += (self.x_velo * time) 
            return self.x_pos 
            

        def ball_y_pos(time):
            self.y_velo = self.magnitude * sin(self.angle)
            self.y_pos += (self.y_velo * time) + ((1/2)*self.y_acc*(time**2))
            return self.y_pos

        return ball_x_pos(time), ball_y_pos(time)


#class Ball:
        

Canon = Canon(45, 35)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(100):
        ball_x, ball_y = Canon.launch(i)
        pygame.draw.circle(window, (0,138, 255), (ball_x, ball_y), 20)
        print(ball_x, ball_y)
   

    clock.tick(60)
    pygame.display.update()



