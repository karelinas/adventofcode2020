#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 09

Usage:

    python3 main.py < input.txt
"""

from sys import stdin
from itertools import combinations


def encryption_weakness(nums, target):
    for start in range(len(nums)):
        for end in range(start+1, len(nums)):
            slice_sum = sum(nums[start:end])
            if slice_sum == target:
                return min(nums[start:end])+max(nums[start:end])
            elif slice_sum > target:
                break
    return None


SLICE_LEN = 25

numbers = [int(line.strip()) for line in stdin]

invalid_sum = next(n for i, n in enumerate(numbers[SLICE_LEN:], SLICE_LEN)
                   if n not in set(a+b for a, b in combinations(numbers[i-SLICE_LEN:i], 2)))

print("Part one:", invalid_sum)
print("Part two:", encryption_weakness(numbers, invalid_sum))
