#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 10

Usage:

    python3 main.py < input.txt
"""

from functools import lru_cache
from itertools import takewhile
from sys import stdin


def arrangement_count(adapters, latest=0):
    @lru_cache(maxsize=None)
    def _impl(_latest):
        if _latest == (len(adapters) - 1):
            return 1
        return sum(_impl(next_adapter)
                   for next_adapter
                   in takewhile(lambda x: adapters[x] - adapters[_latest] <= 3,
                                range(_latest+1, len(adapters))))

    return _impl(latest)


adapters = [0] + sorted(int(line.strip()) for line in stdin)
adapters.append(adapters[-1] + 3)

differences = [b-a for a, b in zip(adapters, adapters[1:])]

print("Part one:", differences.count(1) * differences.count(3))
print("Part two:", arrangement_count(adapters))
