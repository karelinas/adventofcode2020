#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 05

Usage:

    python3 main.py < input.txt
"""

from sys import stdin


def seat_id(boardingpass):
    row = int(boardingpass[:7].replace('F', '0').replace('B', '1'), 2)
    column = int(boardingpass[7:].replace('L', '0').replace('R', '1'), 2)
    return row*8 + column


boardingpasses = (line.strip() for line in stdin)
seat_ids = sorted(seat_id(bp) for bp in boardingpasses)

print("Part one:", seat_ids[-1])
print("Part two:", sum(range(seat_ids[0], seat_ids[-1]+1)) - sum(seat_ids))

