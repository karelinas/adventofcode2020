#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 03

Run with:

    python3 main.py < input.txt
"""

from functools import reduce
from operator import mul
from sys import stdin


def is_tree(grid, x, y):
    width = len(grid[0])
    return grid[y][x%width] == '#'


def tree_count(grid, path):
    return [is_tree(grid, x, y) for x, y in path].count(True)


def simple_path(dx, dy, height):
    x, y = 0, 0
    while y < height:
        yield (x, y)
        x = x + dx
        y = y + dy


def product(lst):
    return reduce(mul, lst, 1)


grid = [line.strip() for line in stdin]
height = len(grid)

print("Part one:", tree_count(grid, simple_path(3, 1, height)))

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]
print("Part two:", product([tree_count(grid, simple_path(dx, dy, height)) for dx, dy in slopes]))
