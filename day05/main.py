#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 05

Run with:

    python3 main.py < input.txt
"""

from sys import stdin


def lower_half(r):
    return (r[0], (r[0]+r[1])//2)


def upper_half(r):
    return ((r[0]+r[1])//2+1, r[1])


def seat_id(boardingpass, region=None):
    if not region:
        region = [(0, 127), (0, 7)]
    if not boardingpass:
        return region[0][0] * 8 + region[1][0]
    char = boardingpass[0]
    if char == 'F':
        region[0] = lower_half(region[0])
    elif char == 'B':
        region[0] = upper_half(region[0])
    elif char == 'L':
        region[1] = lower_half(region[1])
    elif char == 'R':
        region[1] = upper_half(region[1])
    return seat_id(boardingpass[1:], region)


boardingpasses = (line.strip() for line in stdin)
seat_ids = sorted(seat_id(bp) for bp in boardingpasses)

print("Part one:", seat_ids[-1])
print("Part two:", sum(range(seat_ids[0], seat_ids[-1]+1)) - sum(seat_ids))

