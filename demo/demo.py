#!/usr/local/bin/python

import argparse
import sys
import os, math

sys.path.append(os.path.realpath(os.path.dirname(__file__) + '/../..'))

import LSystem


FLAGS = None

systems = {
    'koch': {
        'class': LSystem.Systems.Koch,
        'steps': 7,
        'angle': 90,
        'symbols': ['F']
    },
    'sierpinski': {
        'class': LSystem.Systems.Sierpinski,
        'steps': 7,
        'angle': 120,
        'symbols': ['F', 'G']
    },
    'dragon': {
        'class': LSystem.Systems.Dragon,
        'steps': 16,
        'angle': 90,
        'symbols': ['X', 'Y']
    },
    'twin-dragon': {
        'class': LSystem.Systems.TwinDragon,
        'steps': 15,
        'angle': 90,
        'symbols': ['X', 'Y']
    },
    'levy': {
        'class': LSystem.Systems.Levy,
        'steps': 15,
        'angle': 45,
        'symbols': ['F']
    },
    'hilbert': {
        'class': LSystem.Systems.Hilbert,
        'steps': 7,
        'angle': 90,
        'symbols': ['F'],
        'left': 90
    },
    'hex-gosper': {
        'class': LSystem.Systems.HexagonalGosper,
        'steps': 5,
        'angle': 60,
        'symbols': ['X', 'Y'],
    },
    'crystal': {
        'class': LSystem.Systems.Crystal,
        'steps': 6,
        'angle': 90,
        'symbols': ['F'],
        'left': 90
    },
    'weed': {
        'class': LSystem.Systems.Weed,
        'steps': 6,
        'angle': 22.5,
        'symbols': ['F'],
        'left': 90
    },
    'rings': {
        'class': LSystem.Systems.Rings,
        'steps': 4,
        'angle': 90,
        'symbols': ['F']
    },
    'tiles': {
        'class': LSystem.Systems.Tiles,
        'steps': 5,
        'angle': 90,
        'symbols': ['F']
    },
    'board': {
        'class': LSystem.Systems.Board,
        'steps': 4,
        'angle': 90,
        'symbols': ['F']
    },
    'krishna': {
        'class': LSystem.Systems.KrishnaAnklets,
        'steps': 6,
        'angle': 45,
        'left': 45,
        'symbols': ['F']
    },
    'algae2': {
        'class': LSystem.Systems.Algae2,
        'steps': 16,
        'angle': 12,
        'left': 90,
        'symbols': ['F']
    },
    'qki': {
        'class': LSystem.Systems.QuadraticKochIsland,
        'steps': 3,
        'angle': 90,
        'left': 90,
        'symbols': ['F']
    },
    'triangle': {
        'class': LSystem.Systems.Triangle,
        'steps': 7,
        'angle': 120,
        'left': 90,
        'symbols': ['F']
    }
}

def main(_):

    if FLAGS.system is None:
        raise RuntimeError('Please set the --system value')

    if not FLAGS.system in systems.keys():
        raise RuntimeError('Invalid --system value')

    system = systems[FLAGS.system]
    g = system['class']()
    print str(g.pretty())

    g.run(system['steps'])
    angle = system['angle']
    start = [0, 0]
    step = 1
    draw_symbols = system['symbols']

    cur_angle = angle
    (x, y) = start
    min_x = min_y = max_x = max_y = 0
    path = []

    stack = []

    if 'right' in system: cur_angle += system['right']
    if 'left' in system: cur_angle -= system['left']

    for c in str(g.string):
        if c in draw_symbols:
            a = math.radians(cur_angle)
            x += math.cos(a) * step
            y += math.sin(a) * step
            if x > max_x: max_x = x
            elif x < min_x: min_x = x
            if y > max_y: max_y = y
            elif y < min_y: min_y = y
            path.append([x, y])
        elif c == '-':
            cur_angle += angle
        elif c == '+':
            cur_angle -= angle
        elif c == '[':
            stack.append([x, y, cur_angle])
        elif c == ']':
            if len(stack):
                state = stack.pop()
                x = state[0]
                y = state[1]
                cur_angle = state[2]

    import pygame
    from map.drawer import Drawable, Plotter
    from map.utils import hex_to_rgb

    class MyDrawer(Drawable):
        def __init__(self, path, color = '#000000'):
            self.path = path
            self.color = hex_to_rgb(color)
            self.old_pos = None
            self.offset = [500, 800]
            self.zoom = 2

        def draw(self, screen):
            scale_x = screen.get_width() / (max_x - min_x)
            scale_y = screen.get_height() / (max_y - min_y)
            offset_x = -scale_x * min_x
            offset_y = -scale_y * min_y

            def project(point):
                (x, y) = point
                return [scale_x * x + offset_x, scale_y * y + offset_y]

            try:
                i = iter(self.path)
                old_pos = None
                while True:
                    if not old_pos:
                        old_pos = project(i.next())
                    pos = project(i.next())
                    pygame.draw.line(screen, self.color, old_pos, pos, 1)
                    old_pos = pos
            except StopIteration as e:
                pass

    plotter = Plotter()
    plotter.add_drawer(MyDrawer(path))
    plotter.draw()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--system', type=str, help='LSystem to show [%s]' % ', '.join(systems.keys()))
    FLAGS, unparsed = parser.parse_known_args()
    main([sys.argv[0]] + unparsed)
