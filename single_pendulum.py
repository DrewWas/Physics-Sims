import pygame

WIDTH, HEIGHT = (600,600)
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("single pendulum")

# constants
FPS = 60
black = (0,0,0)
blue = (0, 138, 255)
white = (255,255,255)


def draw():
    WIN.fill(black)
    pygame.draw.rect(WIN, blue, (100,100,100,100))

    pygame.display.update()





def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()
        clock.tick(FPS)



main()



