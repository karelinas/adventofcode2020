#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 15

Usage:

    python3 main.py
"""

from collections import deque
from itertools import count


def number_game(starting_numbers):
    queue = deque(starting_numbers.copy())
    history = {}
    for turn in count():
        said = queue.popleft()
        if not queue:
            queue.append(turn - history.get(said, turn))
        history[said] = turn
        yield said


def nth_turn(game, n):
    return next(val for i, val in enumerate(game, 1) if i == n)


if __name__ == '__main__':
    starting_numbers = [16, 11, 15, 0, 1, 7]
    print("Part one:", nth_turn(number_game(starting_numbers), 2020))
    print("Part two:", nth_turn(number_game(starting_numbers), 30000000))
