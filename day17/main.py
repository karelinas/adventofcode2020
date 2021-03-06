#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 17

Usage: python3 main.py < input.txt
"""

from collections import Counter
from itertools import product
from operator import add
from sys import stdin


def vector_add(v1, v2):
    return tuple(map(add, v1, v2))


def adjacent(vec):
    origin = tuple(0 for _ in range(len(vec)))
    return {
        vector_add(vec, delta)
        for delta in product([-1, 0, 1], repeat=len(vec))
        if delta != origin
    }


def simulate(active_cubes):
    # Neighbor counts for all cells
    neighbors = Counter(pos for vec in active_cubes for pos in adjacent(vec))

    # Resolve active cubes
    return {
        pos
        for pos, count in neighbors.items()
        if count == 3 or (count == 2 and pos in active_cubes)
    }


def chain_call(N, f, *args):
    return f(*args) if N <= 1 else f(chain_call(N-1, f, *args))


if __name__ == '__main__':
    # Read input
    CUBES2D = {
        (x, y)
        for y, line in enumerate(stdin)
        for x, ch in enumerate(line.strip())
        if ch == '#'
    }

    # Part 1: 3D simulation
    CUBES3D = {(x, y, 0) for x, y in CUBES2D}
    print("Part two:", len(chain_call(6, simulate, CUBES3D)))

    # Part 2: 4D simulation
    CUBES4D = {(x, y, 0, 0) for x, y in CUBES2D}
    print("Part two:", len(chain_call(6, simulate, CUBES4D)))
