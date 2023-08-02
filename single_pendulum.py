import pygame

WIDTH, HEIGHT = (800,800)
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("single pendulum")


# constants
FPS = 60
ROPELEN = 300
BALL_MASS = 10  # kg
black = (0,0,0)
blue = (0, 138, 255)
white = (255,255,255)
red = (255,23,54)
gray = (130,130,130)
middle_block_pos = (402, 373)


def getpos():
    from math import acos, cos, sin, degrees
    pos = pygame.mouse.get_pos()

    # get the angle from the square the 'pos' is and then draw the
    # circle at that same angle from the square ROPELEN away 

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


    print("cos degrees: " + str(degrees(theta)))

    print(ROPELEN * sin(theta))
    print(ROPELEN * cos(theta))

    coord = ((ROPELEN * sin(theta) + middle_block_pos[0]), (ROPELEN *
cos(theta) + middle_block_pos[1]))


    return coord



def draw(ball_pos):
    WIN.fill(black)
    pygame.draw.rect(WIN, red, (398, 370, 10, 10))

    # draw the ball and have it be moveable 
    pygame.draw.circle(WIN, blue, ball_pos, 15)

    # draw a line connecting the ball to the square at all times
    pygame.draw.line(WIN, gray, middle_block_pos, ball_pos)




    # ball can only move along the path of the string (this sim assumes
    # a tought line)

    pygame.display.update()




def main():
    run = True
    final_pos = False
    clock = pygame.time.Clock()


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN :
                final_pos = not final_pos



        if final_pos == False:
            ball_pos = getpos()


        draw(ball_pos)
        clock.tick(FPS)



main()



