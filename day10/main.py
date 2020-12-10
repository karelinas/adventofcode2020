#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 10

Usage:

    python3 main.py < input.txt
"""

from collections import Counter
from functools import lru_cache
from sys import stdin


def arrangement_count(adapters):
    @lru_cache(maxsize=None)
    def _impl(n):
        if n not in adapters:
            return 0
        elif n == adapters[-1]:
            return 1
        return sum(_impl(n) for n in [n+1, n+2, n+3])

    return _impl(0)


adapters = [0] + sorted(int(line.strip()) for line in stdin)
adapters.append(adapters[-1] + 3)

differences = Counter(b-a for a, b in zip(adapters, adapters[1:]))

print("Part one:", differences.get(1) * differences.get(3))
print("Part two:", arrangement_count(adapters))
