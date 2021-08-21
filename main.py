import pygame
import sys
import random
from spinner import show_spinner_board, show_spinner

# initialization of pygame window

pygame.init()

width = 800
height = 800

display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption('Spinner')
background = (240, 240, 240)

pygame.init()

# close the window
def close():
    pygame.quit()
    sys.exit()

while True:
    show_spinner_board(display, 6)
    pygame.display.flip()

    angle = 0
    spinning = True

    speed = 0.0
    friction = 0.5

    while spinning:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.MOUSEBUTTONUP:
                speed += random.randrange(40, 75, 1)
                if speed > 100:
                    speed = 100

        speed -= friction

        if speed < 0:
            speed = 0.0

        display.fill(background)
        show_spinner_board(display, 12)

        angle += speed

        show_spinner(display, angle, 'black')

        pygame.display.update()
        clock.tick(120)
