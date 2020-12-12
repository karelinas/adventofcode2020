#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 12

Usage:

    python3 main.py < input.txt
"""

from sys import stdin

def manhattan_distance(z):
    return int(abs(z.real) + abs(z.imag))

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

instructions = map(lambda x: (x[0], int(x[1:])), stdin)

# For part one
facing = complex(DIRECTIONS['E'])
pos1 = complex()
# For part two
waypoint = 10+1j
pos2 = complex()

for action, value in instructions:
    if action in DIRECTIONS:
        pos1 = pos1 + value * complex(DIRECTIONS[action])
        waypoint = waypoint + value * complex(DIRECTIONS[action])
    elif action in ROTATIONS:
        facing = facing * (ROTATIONS[action] ** (value // 90))
        waypoint = waypoint * (ROTATIONS[action] ** (value // 90))
    elif action == 'F':
        pos1 = pos1 + facing * value
        pos2 = pos2 + waypoint * value

print("Part one:", manhattan_distance(pos1))
print("Part two:", manhattan_distance(pos2))
