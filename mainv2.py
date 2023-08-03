import pygame
import math
import numpy as np
import random
from shape_generators import Generators

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


def get_projection(stars: np.ndarray):
    relative_pos = stars - player_pos
    visible = relative_pos[relative_pos[:, 0] > 0]
    brightness = np.minimum(MAG_bright/visible[:, 0], 255)

    # Potentially add code here that will cut out the zero brightness stars!
    size_prj = MAG_rad/visible[:, 0]
    cords = visible[:, 1:]*tan_scale/visible[:, 0]
    cords+=base_line

    return cords, size_prj, brightness


def rotate(stars: np.ndarray, plus: bool, dir="Vertical"):
    poses = stars - player_pos if true_rotation else stars

    if dir == "Horizontal":

        poses[:, :2] = np.matmul(poses[:, :2], R_z_plus.T) if plus else \
            np.matmul(poses[:, :2], R_z_minus.T)

        stars[:, 2] = poses[:, :2] + player_pos[:2] if true_rotation else \
            poses[:, :2]

    if dir == "Vertical":
        poses[:, 0:3:2] = np.matmul(poses[:, 0:3:2], R_z_plus.T) if plus else \
            np.matmul(poses[:, 0:3:2], R_z_minus.T)

        stars[:, 0:3:2] = poses[:, 0:3:2] + player_pos[:2] if true_rotation else \
            poses[:, 0:3:2]

star_num = 6000

# CREATE STAR FIELD HERE

