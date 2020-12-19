#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 01

Usage: python3 main.py < input.txt
"""

from sys import stdin
from itertools import combinations

data = [int(x) for x in stdin]
needle = 2020

print("Part one:", next(a*b for a, b in combinations(data, 2) if a+b==needle))
print("Part two:", next(a*b*c for a, b, c in combinations(data, 3) if a+b+c==needle))
