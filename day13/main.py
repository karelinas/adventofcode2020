#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 13

Usage:

    python3 main.py < input.txt
"""

from itertools import count
from sys import stdin


def next_to_leave(timestamp, buses):
    bus, leaves = next((bus, t)
                       for t in range(timestamp, timestamp+max(buses)+1)
                       for bus in buses
                       if t % bus == 0)
    return (leaves - timestamp) * bus


def earliest_subsequent(bus_offsets):
    timestamp, increment = 0, 1
    for offset, bus in bus_offsets:
        timestamp = next(t for t in count(timestamp, increment) if (t + offset) % bus == 0)
        increment = increment * bus
    return timestamp


timestamp = int(next(stdin))
bus_offsets = [(offset, int(bus)) for offset, bus in enumerate(next(stdin).split(',')) if bus != 'x']

print("Part one:", next_to_leave(timestamp, [bus for _, bus in bus_offsets]))
print("Part two:", earliest_subsequent(bus_offsets))
