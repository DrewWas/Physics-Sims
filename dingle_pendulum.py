import pygame

WIDTH, HEIGHT = (800, 800)
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pendulum")

run = True


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(



"""
PLAN:

* Draw a single block to the screen (anchor point)

* Draw a ball to the screen with variable x and y coords

* The ball is moveable by the mouse until a click
	- After the click, the x and y coords are locked

* The x and y coords of the ball are updateable

* Do the math on forces (even tho some may not be visually present)

* Attach string

"""




