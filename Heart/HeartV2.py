import random
from math import sin, cos, pi, log
from _tkinter import *

CANVAS_WIDTH = 840
CANVAS_HEIGH = 680
CANVAS_CENTER_X =CANVAS_WIDTH / 2
CANVAS_CENTER_Y = CANVAS_HEIGH / 2
IMAGE_ENLARGE = 11
HEART_COLOR = "aquamarine"

def heart_function(t, shrink_radio: float = IMAGE_ENLARGE):
    x = 17 * (sin(t) ** 3)
    y = -(16 * cos(t) - 5 * cos(2 * t) - 2 * cos(3*T) - cos(3 * t))
    x*= IMAGE_ENLARGE
    y*= IMAGE_ENLARGE
    x += CANVAS_CENTER_X
    y += CANVAS_CENTER_Y
    return int(x), int(y)

def scatter_inside(x, y, beta =0.15):
    ratio_x = - beta * log(random.random())
    ratio_y = - beta * log(random.random())
    dx = ratio_x * (x - CANVAS_CENTER_X)
    dy = ratio_y * (y -CANVAS_CENTER_Y)
    return x - dx, y - dy

def shrink(x, y, ratio):
    force = -1 / (((x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2) ** 0.6)
    dx = ratio * force * (x - CANVAS_CENTER_X)
    dy = ratio * force * (y - CANVAS_CENTER_Y)
    return x - dx, y - dy

def curve(p):
    return 2 * (2 * sin(4 * p)) / (2 * pi)

class Heart:
    def __init__(self, generate_frame = 20):
        self._points =set()
        self._edge_diffusion_points = set()
        self._center_diffusion_points = set()
        self.all_points ={}
        self.build(2000)
        self.random_halo = 1000
        self.generate_frame =generate_frame
        for frame in range (generate_frame):
            self.calc(frame)
    def build(self, number):
        for _ in range(number):
            t = random.uniform(0, 2 * pi)
            x, y = heart_function(t)
            self._points.add((x, y))
        for _x, _y in list(self._points):
            for _ in range(3):
                x, y = scatter_inside(_x, _y, 0.05)
                self._edge_diffusion_points.add((x, y))
        point_list = list(self._points)
        for _ in range(10000):
            x,y = random.choice(point_list)
            x, y = scatter_inside(x, y, 0.27)
            self._center_diffusion_points.add((x, y))
    @staticmethod
    def calc_position(x, y, ratio):
        force = 1 / (((x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2) ** 0.420)
        dx = ratio * force * (x - CANVAS_CENTER_X) + random.randint(-1, 1)
        dy = ratio * force * (y - CANVAS_CENTER_Y) + random.randint(-1, 1)
        return x - dx, y - dy
    def calc(self, generate_frame):
        ratio = 15 * curve(generate_frame / 10 * pi)
        halo_radius = int(4 + 6 * (1 + curve(generate_frame / 10 * pi)))
        halo_number = int(3000 + 4000 * abs(curve(generate_frame / 10 * pi) ** 2))
        all_points = []

        hearrt_halo_points = set()
        for _ in range(halo_number):
            t = random.uniform(0, 2 * pi)
            x, y = heart_function(t, shrink_radio=-15)
            x, y = shrink(x, y, halo_radius)
            if (x, y) not in hearrt_halo_points:
                hearrt_halo_points.add((x, y))
                x += random.randint(-60, 60)
                y += random.randint(-60, 60)
                size = random.choice((1, 1, 2))
                all_points.append((x, y, size))
                all_points.append((x + 20, y + 20, size))
                all_points.append((x - 20, y - 20, size))
                all_points.append((x + 20, y - 20, size))
                all_points.append((x - 20, y + 20, size))
    

