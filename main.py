import pygame
import math
import numpy as np
import random
from shape_generators import Generators
import multiprocessing

pygame.init()

# Pixel size of generated screen, generated
WIDTH = 1600
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star Field")

player_pos = np.array([0., 0., 0.])  # Will be ysed to traverse the terrain

# Used to calculate the projection of each star onto the given screen,
# normalised so that the given image is independant of wdt
FOV = 0.6  # Percentage of 180 degrees that is visible
tan_scale = WIDTH / (2 * math.tan(FOV * math.pi / 2))
clock = pygame.time.Clock()
MAG_rad = 400  # Sets projection size of stars
MAG_bright = 150 * 255
running = True
FPS = 30
velocity = np.array([0., 0.])
draw_radius = 400
nnn = WIDTH * 100
base_line = np.array([WIDTH / 2, HEIGHT / 2])

true_rotation = False  # Determines whether object is rotated from the origin
# or whether its rotated from the users perspective

scale1 = draw_radius / 10

angle_steppers = 0.05
STEPPERS = 10

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_q,
    K_e,
)


def generate_r_z(step):
    c = math.cos(step)
    s = math.sin(step)
    R = np.array([[c, -s], [s, c]])
    return R


R_z_minus = generate_r_z(angle_steppers)
R_z_plus = generate_r_z(-angle_steppers)

MAG2 = MAG_bright * MAG_bright / 500


class Star:
    def __init__(self, position=None, size=2):

        if position is None:
            # self.position = np.random.randint(-draw_radius, draw_radius, 3)
            self.position = Generators.torus_generator()
            self.size = size

    def get_projection(self):
        # For now lets not change orientation of camera, facing in positive x
        # direction
        relative_position = self.position - player_pos

        # self.replace(relative_position)

        if relative_position[0] <= 0:
            return None
        else:
            brightness = min(MAG_bright / relative_position[0],
                             255)
            if brightness == 0:
                return None
            size_prj = MAG_rad / relative_position[0]

            # cord = np.array([relative_position[1], relative_position[
            #     2]*math.sin(size_prj/5)]) * (
            #         tan_scale/relative_position[0])
            # cord[1] = cord[1]*cord[0]/255

            cord = np.array([relative_position[1], relative_position[
                2]]) * (tan_scale / relative_position[0])

            cord += base_line
            if not (0 <= cord[0] < WIDTH and 0 <= cord[1] < HEIGHT):
                return None

            return tuple(cord), size_prj, brightness

    def replace(self, relative_position):
        if np.dot(relative_position, relative_position) \
                > 4 * draw_radius * draw_radius and False:
            rand_sign = 2 * np.random.randint(0, 2, 3) - 1
            dist = np.random.randint(draw_radius, draw_radius * 2, 3)
            rand_dev = np.multiply(rand_sign, dist)
            dim = list(range(3))
            dim.remove(random.randint(0, 2))
            for x in dim:
                rand_dev[random.randint(0, 2)] = random.randint(-draw_radius,
                                                                draw_radius)

            self.position = player_pos + rand_dev


def rotate(star: Star, plus: bool, dir="Vertical"):
    relative_pos = star.position - player_pos if true_rotation else \
        star.position

    if dir == "Horizontal":
        relative_pos[:2] = R_z_plus.dot(relative_pos[:2]) if plus else \
            R_z_minus.dot(relative_pos[:2])
        star.position[:2] = relative_pos[:2] + player_pos[:2] if true_rotation \
            else relative_pos[:2]

    elif dir == "Vertical":
        relative_pos[0:3:2] = R_z_plus.dot(relative_pos[0:3:2]) if plus else \
            R_z_minus.dot(relative_pos[0:3:2])
        star.position[0:3:2] = relative_pos[0:3:2] + player_pos[0:3:2] if \
            true_rotation else relative_pos[0:3:2]


star_num = 6000
star_field = [Star() for i in range(star_num)]

while running:
    # Use this to get events

    keys = pygame.key.get_pressed()

    plus_rotate_ho = False
    minus_rotate_ho = False
    plus_rotate_ve = False
    minus_rotate_ve = False

    if keys[pygame.K_UP]:
        velocity[0] += STEPPERS
    if keys[pygame.K_DOWN]:
        velocity[0] -= STEPPERS
    if keys[pygame.K_LEFT]:
        velocity[1] -= STEPPERS
    if keys[pygame.K_RIGHT]:
        velocity[1] += STEPPERS
    if keys[pygame.K_d]:
        plus_rotate_ho = True
    if keys[pygame.K_a]:
        minus_rotate_ho = True
    if keys[pygame.K_s]:
        plus_rotate_ve = True
    if keys[pygame.K_w]:
        minus_rotate_ve = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print('hhh')
            if event.key == K_q:
                FOV -= 0.05
            elif event.key == K_e:
                FOV += 0.05
            tan_scale = WIDTH / (2 * math.tan(FOV * math.pi / 2))

    player_pos[0] += velocity[0] / FPS
    player_pos[1] += velocity[1] / FPS
    screen.fill((10, 10, 10))

    for x in star_field:
        if plus_rotate_ho:
            rotate(x, True, dir="Horizontal")
        if minus_rotate_ho:
            rotate(x, False, dir="Horizontal")
        if plus_rotate_ve:
            rotate(x, True, dir="Vertical")
        if minus_rotate_ve:
            rotate(x, False, dir="Vertical")

        u = x.get_projection()
        if u is not None:
            coordinates, prj_size, brightness = u
            pygame.draw.circle(surface=screen, center=coordinates,
                               radius=prj_size, color=(brightness, brightness,
                                                       brightness))

    pygame.display.flip()
    clock.tick(FPS)
