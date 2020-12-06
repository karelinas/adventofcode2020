#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 03

Usage:

    python3 main.py < input.txt
"""

from functools import reduce
from operator import mul
from sys import stdin


def tree_count(grid, path):
    return sum(grid[y][x] for x, y in path)


def xwrapping_path(vx, vy, width, height):
    x, y = 0, 0
    while y < height:
        yield (x%width, y)
        x, y = x+vx, y+vy


def product(lst):
    return reduce(mul, lst, 1)


cell_values = {'.': 0, '#': 1}
grid = [[cell_values.get(ch) for ch in line.strip()] for line in stdin]
size = (len(grid[0]), len(grid))

print("Part one:", tree_count(grid, xwrapping_path(3, 1, *size)))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print("Part two:", product(tree_count(grid, xwrapping_path(*v, *size)) for v in slopes))
