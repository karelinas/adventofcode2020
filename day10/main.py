#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 10

Usage:

    python3 main.py < input.txt
"""

from collections import Counter, defaultdict
from sys import stdin


def arrangement_count(adapters):
    counts = defaultdict(int)
    counts[0] = 1
    for n in adapters[1:]:
        counts[n] = counts[n-1] + counts[n-2] + counts[n-3]
    return counts[max(adapters)]


adapters = [0] + sorted(int(line.strip()) for line in stdin)
adapters.append(adapters[-1] + 3)

differences = Counter(b-a for a, b in zip(adapters, adapters[1:]))

print("Part one:", differences.get(1) * differences.get(3))
print("Part two:", arrangement_count(adapters))
