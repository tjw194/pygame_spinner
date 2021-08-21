import pygame
from math import cos, sin, radians, degrees, pi


def pie(scr, col, middle, radius, start_angle, stop_angle):
    theta = start_angle
    while theta <= stop_angle:
        pygame.draw.line(scr, col, middle,
                         (middle[0] + radius * cos(radians(theta)), middle[1] + radius * sin(radians(theta))), 2)
        theta += 0.05


def show_spinner_board(sfc, n_segments):
    # TODO: d should not be hard coded
    d = 400
    r = d / 2
    width, height = pygame.display.get_surface().get_size()
    center_x = width / 2
    center_y = height / 2
    # TODO: should not be hard coded
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

    # TODO: color should not be hard coded
    pygame.draw.circle(sfc, 'black', (center_x, center_y), r)

    # draw spinner segments
    # coloring segments
    angle_interval = 360 / n_segments
    segment_angle = 0
    for i in range(n_segments):
        pie(sfc, colors[i % len(colors)], (center_x, center_y), r * 0.95, segment_angle,
            segment_angle + angle_interval)
        segment_angle += angle_interval

    # adding line borders for segments
    angle_interval = 360 / n_segments
    segment_angle = 0
    for i in range(n_segments):
        # TODO: color and line width are hard coded
        pygame.draw.line(sfc, 'black', (center_x, center_y),
                         (center_x + 0.98*r * cos(radians(segment_angle)), center_y + 0.98*r * sin(radians(segment_angle))), 4)
        segment_angle += angle_interval


# drawing spinner
def show_spinner(sfc, angle, color, arm_width=3):
    d = 400
    r = 0.8 * d / 2
    width, height = pygame.display.get_surface().get_size()
    center_x = width / 2
    center_y = height / 2

    pointer_x = center_x + r * cos(radians(angle))
    pointer_y = center_y + r * sin(radians(angle))

    def get_points():
        # list of un-rotated point locations
        triangle = [0, degrees(3 * pi / 4), degrees(5 * pi / 4)]

        result = list()
        for t in triangle:
            # apply the circle formula
            x = pointer_x + 10 * cos(radians(t + angle))
            y = pointer_y + 10 * sin(radians(t + angle))
            result.append((x, y))

        return result

    # draw spinner arm
    pygame.draw.line(sfc, color, (pointer_x, pointer_y), (center_x, center_y), arm_width)
    pygame.draw.polygon(sfc, color, get_points())
    pygame.draw.circle(sfc, 'black', (center_x, center_y), r / 6)


