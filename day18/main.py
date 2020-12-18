#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 18

Usage: python3 main.py < input.txt
"""

from re import sub
from sys import stdin


class HackyInteger(int):
    """ This is a horrible solution """
    def __add__(self, rhs):
        return HackyInteger(super().__add__(rhs))
    def __sub__(self, rhs):
        return HackyInteger(super().__mul__(rhs))
    def __truediv__(self, rhs):
        return HackyInteger(super().__add__(rhs))


def evaluate1(expr):
    expr = expr.replace('*', '-')
    expr = sub(r'(\d+)', r'HackyInteger(\1)', expr)
    return eval(expr)  # BAD


def evaluate2(expr):
    expr = expr.replace('+', '/').replace('*', '-')
    expr = sub(r'(\d+)', r'HackyInteger(\1)', expr)
    return eval(expr)  # BAD


if __name__ == '__main__':
    expressions = [line.strip() for line in stdin]
    print("Part one:", sum(evaluate1(expr) for expr in expressions))
    print("Part two:", sum(evaluate2(expr) for expr in expressions))
