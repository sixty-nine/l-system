#!/usr/local/bin/python

import argparse
import sys
import os, math
import turtle
from turtle import *

sys.path.append(os.path.realpath(os.path.dirname(__file__) + '/../..'))

import LSystem


FLAGS = None

systems = {
    'koch': {
        'class': LSystem.Systems.Koch,
        'steps': 7,
        'angle': 90,
        'pos': [-500, -400],
        'len': 2,
        'symbols': ['F']
    },
    'sierpinski': {
        'class': LSystem.Systems.Sierpinski,
        'steps': 7,
        'angle': 120,
        'pos': [-600, 400],
        'len': 7,
        'symbols': ['F', 'G']
    },
    'dragon': {
        'class': LSystem.Systems.Dragon,
        'steps': 14,
        'angle': 90,
        'pos': [0, 0],
        'len': 7,
        'symbols': ['X', 'Y']
    },
    'hilbert': {
        'class': LSystem.Systems.Hilbert,
        'steps': 7,
        'angle': 90,
        'pos': [-400, -300],
        'len': 7,
        'symbols': ['F'],
        'left': 90
    },
    'hex-gosper': {
        'class': LSystem.Systems.HexagonalGosper,
        'steps': 7,
        'angle': 60,
        'pos': [250, -300],
        'len': 7,
        'symbols': ['X', 'Y'],
    },
    'crystal': {
        'class': LSystem.Systems.Crystal,
        'steps': 5,
        'angle': 90,
        'pos': [400, -300],
        'len': 3,
        'symbols': ['F'],
        'left': 90
    },
    'weed': {
        'class': LSystem.Systems.Weed,
        'steps': 6,
        'angle': 22.5,
        'pos': [0, -300],
        'len': 5,
        'symbols': ['F'],
        'left': 90
    },
}

def main(_):

    if FLAGS.system is None:
        raise RuntimeError('Please set the --system value')

    if not FLAGS.system in systems.keys():
        raise RuntimeError('Invalid --system value')

    system = systems[FLAGS.system]
    g = system['class']().run(system['steps'])
    angle = system['angle']
    start = system['pos']
    step = system['len']
    draw_symbols = system['symbols']

    if 'left' in system: left(system['left'])
    if 'right' in system: right(system['right'])

    hideturtle()
    speed(0)
    penup()
    setx(start[0])
    sety(start[1])
    pendown()

    stack = []

    for c in str(g.string):
        if c in draw_symbols: forward(step)
        if c == '-': right(angle)
        if c == '+': left(angle)
        if c == '[':
            stack.append([heading(), position()])
        if c == ']':
            if len(stack):
                penup()
                state = stack.pop()
                setheading(state[0])
                setposition(state[1][0], state[1][1])
                pendown()

    done()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--system', type=str, help='LSystem to show [%s]' % ', '.join(systems.keys()))
    FLAGS, unparsed = parser.parse_known_args()
    main([sys.argv[0]] + unparsed)
