import pygame
import sys
import random
from spinner import Spinner, SpinnerArm

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

# creating the spinner object and configuring some options
spinner = Spinner(display, (400, 400), 300, 12)
spinner.colors = ['blue', 'gray', 'brown']
spinner.borders = True

# creating 2 spinner arm objects and configuring some options
arm = SpinnerArm(display, (400, 400), 280)
arm.arm_width = 6
arm2 = SpinnerArm(display, (400, 400), 220)
arm2.arm_color = 'purple4'
arm2.cap_color = 'yellow'

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close()
        if event.type == pygame.MOUSEBUTTONUP:
            # on mouse click, get a random speed for each spinner arm
            arm.speed = random.randrange(40, 75, 1)
            arm2.speed = random.randrange(40, 75, 1)

    # reduce spinner speed based on friction value
    arm.speed -= arm.friction
    arm2.speed -= arm2.friction

    # stop spinning so spinner does not go in reverse direction
    if arm.speed < 0:
        arm.speed = 0.0
    if arm2.speed < 0:
        arm2.speed = 0.0

    # show the spinner board and spinners
    display.fill(background)
    spinner.show()
    arm.show()
    arm2.show()

    # updating angle of each spinner arm
    arm.angle += arm.speed
    arm2.angle += arm2.speed

    pygame.display.update()
    clock.tick()
