#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 11

Usage:

    python3 main.py < input.txt
"""

from functools import lru_cache
from sys import stdin


class Grid(dict):
    FLOOR = '.'
    EMPTY = 'L'
    OCCUPIED = '#'

    def __missing__(self, key):
        return Grid.FLOOR


def cell_seating(coords, cell, neighbors, tolerance):
    if cell == Grid.FLOOR:
        return (coords, Grid.FLOOR)
    elif cell == Grid.EMPTY and all(ch != Grid.OCCUPIED for ch in neighbors):
        return (coords, Grid.OCCUPIED)
    elif cell == Grid.OCCUPIED and neighbors.count(Grid.OCCUPIED) >= tolerance:
        return (coords, Grid.EMPTY)
    return (coords, cell)


def adjacent(grid, x, y):
    return [grid[x-1, y-1], grid[x, y-1], grid[x+1, y-1],
            grid[x-1, y  ],               grid[x+1, y  ],
            grid[x-1, y+1], grid[x, y+1], grid[x+1, y+1]]


@lru_cache(maxsize=None)
def vector_add(a, b):
    return tuple(an+bn for an, bn in zip(a, b))


def line_of_sight(grid, x, y):
    def sees(pos, v):
        pos = vector_add(pos, v)
        while pos in grid:
            if grid[pos] != Grid.FLOOR:
                return grid[pos]
            pos = vector_add(pos, v)
        return None

    vectors = [(-1, -1), (0, -1), (1, -1),
               (-1,  0),          (1,  0),
               (-1,  1), (0,  1), (1,  1)]
    neighbors = [sees((x, y), vec) for vec in vectors]
    return [neighbor for neighbor in neighbors if neighbor]


def seating_round(grid, neighbor_finder, tolerance):
    return Grid(
        cell_seating((x, y), grid[x, y], neighbor_finder(grid, x, y), tolerance)
        for x, y in list(grid.keys())
    )


def stabilized(grid, neighbor_finder, tolerance):
    previous = grid
    while True:
        current = seating_round(previous, neighbor_finder, tolerance)
        if current == previous:
            break
        previous = current
    return current


grid = Grid({(x, y): ch for y, line in enumerate(stdin) for x, ch in enumerate(line.strip())})

print("Part one:", list(stabilized(grid, adjacent, 4).values()).count(Grid.OCCUPIED))
print("Part two:", list(stabilized(grid, line_of_sight, 5).values()).count(Grid.OCCUPIED))
