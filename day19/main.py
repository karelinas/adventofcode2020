#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 19

usage: python3 main.py < input.txt
"""

from itertools import takewhile
from sys import stdin
from re import match


def parsed_rule(txt):
    rulenumber, ruledef = match(r'^(\d+): (.*)$', txt).groups()
    charrule = match(r'^"(\w+)"$', ruledef)
    if charrule:
        return (int(rulenumber), charrule.group(1))
    return (
        int(rulenumber),
        [[int(n) for n in alternative.split()]
         for alternative in ruledef.split('|')]
    )


def check(rules, message):
    return any(not remaining for remaining in check_rule(message, rules, 0))


def check_rule(message, rules, rulenum=0):
    if isinstance(rules[rulenum], list):
        for seq in rules[rulenum]:
            yield from check_subrules(message, rules, seq)
    elif message and message[0] == rules[rulenum]:
        yield message[1:]


def check_subrules(message, rules, subrules):
    if subrules:
        rulenum, *subrules = subrules
        for msg in check_rule(message, rules, rulenum):
            yield from check_subrules(msg, rules, subrules)
    else:
        yield message


if __name__ == '__main__':
    rules = dict(parsed_rule(line) for line in takewhile(lambda s: s.strip(), stdin))
    messages = [s.strip() for s in stdin]

    print("Part one:", sum(check(rules, msg) for msg in messages))

    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    print("Part two:", sum(check(rules, msg) for msg in messages))
