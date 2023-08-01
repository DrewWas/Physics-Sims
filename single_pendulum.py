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
red = (255,23,54)
gray = (130,130,130)



def getpos():
    pos = pygame.mouse.get_pos()
    return (pos)



def draw(ball_pos):
    middle_block_pos = (294, 133)

    WIN.fill(black)
    pygame.draw.rect(WIN, red, (290, 130, 10, 10))

    # draw the ball and have it be moveable 
    pygame.draw.circle(WIN, blue, ball_pos, 15)

    # draw a line connecting the ball to the square at all times
    pygame.draw.line(WIN, gray, middle_block_pos, ball_pos)



    # Upon click, the ball pos (and therefore string) are temporarily
    # locked until the sim starts (spacebar is hit... or any key idk
    # yet)


    # ball can only move along the path of the string (can it move
    # inwards????)

    pygame.display.update()




def main():
    run = True
    final_pos = False
    clock = pygame.time.Clock()


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                final_pos = not final_pos


        if final_pos == False:
            ball_pos = getpos()


        draw(ball_pos)
        clock.tick(FPS)



main()



