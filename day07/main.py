#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 07

Usage: python3 main.py < input.txt
"""

from collections import defaultdict
from functools import reduce
from re import findall, MULTILINE
from sys import stdin


def parsed_rules(data):
    lineregex = r'^(.*) bags contain (no other bags|\d+ .* bags?(?:, \d+ .* bags?)*)\.$'
    innerregex = r'^(\d+) (.*) bags?$'
    return {
        outer: {
                   inner: int(count)
                   for sub in innertxt.split(', ')
                   for count, inner in findall(innerregex, sub)
               }
        for outer, innertxt in findall(lineregex, data, MULTILINE)
    }


def backward_rules(rules):
    def _append_to_key(d, key, val):
        d[key].append(val)
        return d

    return reduce(lambda d, v: _append_to_key(d, v[0], v[1]),
                  [(v, k) for k, vs in rules.items() for v in vs],
                  defaultdict(list))


def connected_nodes(graph, start):
    return set.union(set([start]),
                     *[connected_nodes(graph, nextnode) for nextnode in graph[start]])


def inner_count(rules, start):
    return sum(count*(1 + inner_count(rules, bag)) for bag, count in rules.get(start, {}).items())


rules = parsed_rules(stdin.read())
backward = backward_rules(rules)

print("Part one:", len(connected_nodes(backward, 'shiny gold'))-1)
print("Part two:", inner_count(rules, 'shiny gold'))
