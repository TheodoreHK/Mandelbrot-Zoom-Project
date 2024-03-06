import random
import numpy as np
import matplotlib
import time
from PIL import Image

def make_image(center_num, width):
    image = Image.new("RGB", (128, 128), (255, 255, 255))
    pixels = image.load()
    pixels[64, 64] = dist_to_color(calc(center_num)[1])
    for x in range(128):
        for y in range(128):
            coordinate = (center_num[0] + ((x-64) * (width / 128)), center_num[1] + ((y-64) * (width / 128)))
            pixels[x, y] = dist_to_color(calc(coordinate)[1])


# max_distance is set to 10^8.
def dist_to_color(distance, max_distance):
    if distance >= max_distance:
        return 255, 255, 255



    return 100, 100, 100


# coordinate takes (a, b) pair referring to the a and b in (a + bi).
# coordinate[0] returns the "a" and coordinate[1] returns the b
def calc(coordinate):
    z_500 = recurse_calc(500, coordinate, coordinate)
    distance = np.sqrt((coordinate[0]-z_500[0])**2 + (coordinate[1]-z_500)**2)
    return distance


def recurse_calc(counter, zn, z0):
    if counter == 0:
        return zn
    zn_sqr = (zn[0]**2 - zn[1]**2, 2*zn[0]*zn[1])
    next_coord = zn_sqr[0] + z0[0], zn_sqr[1] + z0[1]
    return recurse_calc(counter-1, next_coord, z0)
