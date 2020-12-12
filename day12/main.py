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
    'N': complex( 1j), # ( 0,  1)
    'S': complex(-1j), # ( 0, -1)
    'W': complex(-1 ), # (-1,  0)
    'E': complex( 1 )  # ( 1,  0)
}

ROTATIONS = {
    'L': complex( 1j),
    'R': complex(-1j)
}

instructions = map(lambda x: (x[0], int(x[1:])), stdin)

facing = DIRECTIONS['E']  # part 1
pos1   = 0j               # part 1

waypoint = 10+1j # part 2
pos2     = 0j    # part 2

for action, value in instructions:
    if action in DIRECTIONS:
        pos1     = pos1     + value * DIRECTIONS[action]  # part 1
        waypoint = waypoint + value * DIRECTIONS[action]  # part 2
    elif action in ROTATIONS:
        facing   = facing   * ROTATIONS[action] ** (value // 90)  # part 1
        waypoint = waypoint * ROTATIONS[action] ** (value // 90)  # part 2
    elif action == 'F':
        pos1 = pos1 + facing   * value  # part 1
        pos2 = pos2 + waypoint * value  # part 2

print("Part one:", manhattan_distance(pos1))
print("Part two:", manhattan_distance(pos2))
