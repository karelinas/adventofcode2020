#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 06

Usage:

    python3 main.py < input.txt
"""

from sys import stdin

answers = [
        list(set(yes for yes in person.strip()) for person in group.split())
        for group in stdin.read().split('\n\n')
]

print("Part one:", sum(len(set.union(*group)) for group in answers))
print("Part two:", sum(len(set.intersection(*group)) for group in answers))
