import pygame
import math
pygame.init()

WIDTH, HEIGHT = 750, 750
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce Fr")
clock = pygame.time.Clock()

blue = (0, 138, 255)
black = (0, 0, 0)


def draw_box(box_width, box_height, color):
    x_pos = (WIDTH // 2) - (box_width // 2)
    y_pos = (WIDTH // 2) - (box_height // 2)
    pygame.draw.rect(window, color, (x_pos, y_pos, box_width, box_height), 5)


def main():
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_box(500,500,blue)
        pygame.display.update()

        clock.tick(60)

main()


