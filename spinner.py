import pygame
from math import cos, sin, radians, degrees, pi


def pie(scr, color, middle, radius, start_angle, stop_angle):
    """
    helper function to draw spinner colored segments
    :param scr: pygame display surface
    :param color: segment color
    :param middle: center of the spinner board to start drawing color
    :param radius: length of colored line (radius of spinner board)
    :param start_angle: start of segment
    :param stop_angle: end of segment
    :return: None
    """
    theta = start_angle
    while theta < stop_angle:
        pygame.draw.line(scr, color, middle,
                         (middle[0] + radius * cos(radians(theta)), middle[1] + radius * sin(radians(theta))), 3)
        theta += 0.05


class Spinner:
    # Spinner class to create background of spinner board
    def __init__(self, pygame_surface, location, radius, number_of_segments):
        """
        init function for spinner board
        :param pygame_surface: pygame surface on which to draw the spinner
        :param location: (x, y) location for center of the spinner board
        :param radius: radius of the spinner board in pixels
        :param number_of_segments: number of segments to draw on the spinner board
        """
        self.pygame_surface = pygame_surface
        self.number_of_segments = number_of_segments
        self.location = location
        self.radius = radius
        self.borders = True
        self.border_color = 'black'
        self.border_width = 4
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

        self.center_x = location[0]
        self.center_y = location[1]

    def show(self):
        # shows spinner board on pygame surface

        # coloring spinner segments based on color list in init function
        angle_interval = 360 / self.number_of_segments
        segment_angle = 0
        for i in range(self.number_of_segments):
            pie(self.pygame_surface, self.colors[i % len(self.colors)], (self.center_x, self.center_y),
                self.radius - self.border_width, segment_angle, segment_angle + angle_interval)
            segment_angle += angle_interval

        # draw outer border
        pygame.draw.circle(self.pygame_surface, self.border_color, (self.center_x, self.center_y), self.radius,
                           self.border_width)

        # adding line borders for segments
        if self.borders:
            segment_angle = 0
            for i in range(self.number_of_segments):
                pygame.draw.line(self.pygame_surface, self.border_color, (self.center_x, self.center_y),
                                 (self.center_x + (self.radius - self.border_width) * cos(radians(segment_angle)),
                                  self.center_y + (self.radius - self.border_width) * sin(radians(segment_angle))), self.border_width)
                segment_angle += angle_interval

        # TODO: add text to spinner segments


class SpinnerArm:
    # SpinnerArm class to draw the pointer
    def __init__(self, pygame_surface, location, radius):
        """
        init function for spinner arm
        :param pygame_surface: pygame surface on which to draw the pointer
        :param location: location: (x, y) location for center of the spinner board
        :param radius: length of the pointer arm
        """
        self.pygame_surface = pygame_surface
        self.location = location
        self.radius = radius
        self.arm_color = 'black'
        self.arm_width = 4
        self.cap_color = 'black'  # small circle in center of spinner
        self.angle = 0
        self.friction = 0.5
        self.speed = 0

        self.center_x = location[0]
        self.center_y = location[1]

    def show(self):

        pointer_x = self.center_x + self.radius * cos(radians(self.angle))
        pointer_y = self.center_y + self.radius * sin(radians(self.angle))

        def get_points():
            # list of un-rotated point locations
            triangle = [0, degrees(3 * pi / 4), degrees(5 * pi / 4)]

            result = list()
            for t in triangle:
                # apply the circle formula
                x = pointer_x + (self.arm_width * 3) * cos(radians(t + self.angle))
                y = pointer_y + (self.arm_width * 3) * sin(radians(t + self.angle))
                result.append((x, y))

            return result

        # draw spinner arm
        pygame.draw.line(self.pygame_surface, self.arm_color, (pointer_x, pointer_y), (self.center_x, self.center_y), self.arm_width)
        pygame.draw.polygon(self.pygame_surface, self.arm_color, get_points())

        # center circle
        pygame.draw.circle(self.pygame_surface, self.cap_color, (self.center_x, self.center_y), self.radius / 20)








