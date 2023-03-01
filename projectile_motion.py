import pygame
pygame.init()

#Set Up
window = pygame.display.set_mode((1200,900))
pygame.display.set_caption("Projectile Motion")
run = True

def draw_ball(x,y):
    pygame.draw.circle(window, (0,138,255), (x,y), 20)
    return None



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw_ball(200,200)
    pygame.display.update()
