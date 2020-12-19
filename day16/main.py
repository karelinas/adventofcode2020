#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 16

Usage: python3 main.py < input.txt
"""

from functools import reduce
from itertools import takewhile
from operator import mul
from re import match
from sys import stdin


def prod(nums):
    return reduce(mul, nums, 1)


def rule(txt):
    mo = match(r'^(.*): (\d+)-(\d+) or (\d+)-(\d+)$', txt)
    r = [t(s) for t, s in zip((str, int, int, int, int), mo.groups())]
    return (
        r[0],
        lambda x: r[1] <= x <= r[2] or r[3] <= x <= r[4]
    )


def valid_ticket(ticket, rules):
    return all(any(check(v) for name, check in rules) for v in ticket)


def real_rules(rules, tickets):
    valid_tickets = [ticket for ticket in tickets if valid_ticket(ticket, rules)]
    narrowed_down = [
        [rule for rule in rules if all(rule[1](v) for v in vals)]
        for vals in map(list, zip(*valid_tickets))
    ]
    final = [None] * len(narrowed_down)
    while None in final:
        i, rule = next((i, l[0]) for i, l in enumerate(narrowed_down) if len(l) == 1)
        for l in narrowed_down:
            if rule in l:
                l.remove(rule)
        final[i] = rule
    return final


def parsed(it):
    rules = [rule(line) for line in takewhile(lambda s: s.strip(), it)]
    assert next(it) == 'your ticket:\n'
    my_ticket = [int(val) for line in takewhile(lambda s: s.strip(), it) for val in line.strip().split(',')]
    assert next(it) == 'nearby tickets:\n'
    nearby_tickets = [[int(val) for val in line.split(',')] for line in it]
    return (rules, my_ticket, nearby_tickets)


if __name__ == '__main__':
    rules, my_ticket, nearby_tickets = parsed(stdin)

    print("Part one:", sum(
        v for ticket in nearby_tickets
        for v in ticket
        if not any(check(v) for name, check in rules)
    ))

    print("Part two:", prod(
        val
        for val, (name, _) in zip(my_ticket, real_rules(rules, nearby_tickets))
        if name.startswith('departure')
    ))
