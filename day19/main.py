#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 19

Usage: python3 main.py < input.txt
"""

from collections import namedtuple
from operator import mul, add
from re import findall
from sys import stdin

Token = namedtuple('Token', ['name', 'value'])

TOKEN_MAP = {
    '+': 'ADD',
    '*': 'MUL',
    '(': 'LPAREN',
    ')': 'RPAREN'
}

OPERATOR_MAP = {
    'ADD': add,
    'MUL': mul
}

def tokenize(expr):
    return [Token(TOKEN_MAP.get(tok, 'NUM'), tok) for tok in findall('\d+|[\*+()]', expr)]

def ast(tokens):
    level = []
    for tok in tokens:
        if tok.name in ('MUL', 'ADD'):
            level.append(tok)
        elif tok.name == 'NUM':
            level.append([tok])
        elif tok.name == 'RPAREN':
            return level
        elif tok.name == 'LPAREN':
            level.append(ast(tokens))
    return level

def evaluate(tree):
    if isinstance(tree, Token):
        return int(tree.value)
    if len(tree) == 1:
        return evaluate(tree[0])
    return OPERATOR_MAP[tree[-2].name](evaluate(tree[:-2]), evaluate(tree[-1:]))

def evaluate2(tree):
    if isinstance(tree, Token):
        return int(tree.value)
    if len(tree) == 1:
        return evaluate2(tree[0])
    try:
        mulpos = next(i for i, node in reversed(list(enumerate(tree))) if isinstance(node, Token) and node.name == 'MUL')
        return OPERATOR_MAP[tree[mulpos].name](evaluate2(tree[:mulpos]), evaluate2(tree[mulpos+1:]))
    except StopIteration:
        return OPERATOR_MAP[tree[-2].name](evaluate2(tree[:-2]), evaluate2(tree[-1:]))



def calc(expr):
    return evaluate(ast(iter(tokenize(expr))))

def calc2(expr):
    return evaluate2(ast(iter(tokenize(expr))))


assert calc('2 * 3 + (4 * 5)') == 26
assert calc('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 437
assert calc('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 12240
assert calc('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632

assert calc2('1 + (2 * 3) + (4 * (5 + 6))') == 51
assert calc2('2 * 3 + (4 * 5)') == 46
assert calc2('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 1445
assert calc2('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 669060
assert calc2('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 23340

expressions = [line for line in stdin]
print("Part one:", sum(calc(expr) for expr in expressions))
print("Part two:", sum(calc2(expr) for expr in expressions))


#[5 + [[[[8 * 3] + 9] + 3] * 4]
