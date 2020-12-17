#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 17

Usage:

    python3 main.py < input.txt
"""

from itertools import product
from functools import lru_cache
from operator import add
from sys import stdin


def vec_add(a, b):
    return tuple(map(add, a, b))


@lru_cache(maxsize=None)
def surrounding(vec):
    origin = tuple(0 for _ in range(len(vec)))
    return set(
        vec_add(vec, delta)
        for delta in product(*[range(-1, 2) for _ in range(len(vec))])
        if delta != origin
    )


def count_active_around(cubes, vec):
    return len(set.intersection(surrounding(vec), cubes))


def simulate(active_cubes):
    new_cubes = set()
    for vec in active_cubes:
        # check if this cube should be activated
        if 2 <= count_active_around(active_cubes, vec) <= 3:
            new_cubes.add(vec)
        # check if any inactive cubes adjacent to this cube should be activated
        for adjacent in surrounding(vec):
            if adjacent not in active_cubes and count_active_around(active_cubes, adjacent) == 3:
                new_cubes.add(adjacent)
    return new_cubes


if __name__ == '__main__':
    CUBES2D = {(x, y) for y, line in enumerate(stdin) for x, ch in enumerate(line.strip()) if ch == '#'}

    # Part 1: 3D simulation
    cubes3d = {(x, y, 0) for x, y in CUBES2D}
    for _ in range(6):
        cubes3d = simulate(cubes3d)
    print("part one:", len(cubes3d))

    # Part 2: 4D simulation
    cubes4d = {(x, y, 0, 0) for x, y in CUBES2D}
    for _ in range(6):
        cubes4d = simulate(cubes4d)
    print("part two:", len(cubes4d))
