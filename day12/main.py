#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 12

Usage:

    python3 main.py < input.txt
"""

from sys import stdin

DIRECTIONS = {
    'N':  1j, # ( 0,  1)
    'S': -1j, # ( 0, -1)
    'W': -1,  # (-1,  0)
    'E':  1   # ( 1,  0)
}

ROTATIONS = {
    'L':  1j,
    'R': -1j
}

instructions = list(map(lambda x: (x[0], int(x[1:])), stdin))

facing = complex(DIRECTIONS['E'])
position = complex()

for action, value in instructions:
    if action in DIRECTIONS:
        position = position + value * complex(DIRECTIONS[action])
    elif action in ROTATIONS:
        facing = facing * (ROTATIONS[action] ** (value // 90))
    elif action == 'F':
        position = position + facing * value


print("Part one:", int(abs(position.real) + abs(position.imag)))


position = complex()
waypoint = 10+1j

for action, value in instructions:
    if action in DIRECTIONS:
        waypoint = waypoint + value * complex(DIRECTIONS[action])
    elif action in ROTATIONS:
        waypoint = waypoint * (ROTATIONS[action] ** (value // 90))
    elif action == 'F':
        position = position + waypoint * value

print("Part two:", int(abs(position.real) + abs(position.imag)))
