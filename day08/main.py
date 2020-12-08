#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 08

Usage:

    python3 main.py < input.txt
"""

from re import match
from sys import stdin


def op(line):
    operator, operand = match(r'^(\w+) ([+-]*\d+)$', line).groups()
    return (operator, int(operand))


def run(ops):
    pc = 0
    acc = 0
    seen = set()
    while pc < len(ops):
        op = ops[pc]
        if pc in seen:
            return (False, acc)
        seen.add(pc)
        if op[0] == 'nop':
            pass
        elif op[0] == 'acc':
            acc += op[1]
        elif op[0] == 'jmp':
            pc += op[1]
            continue
        pc += 1
    return (True, acc)


def swap_operator(ops, pos):
    ops = ops.copy()
    op = list(ops[pos])
    if op[0] == 'jmp':
        op[0] = 'nop'
    elif op[0] == 'nop':
        op[0] = 'jmp'
    return ops[:pos] + [tuple(op)] + ops[pos+1:]


program = [op(line) for line in stdin]

terminated, acc = run(program)
print("Part one:", acc)

for i in range(len(program)):
    modified_program = swap_operator(program, i)
    terminated, acc = run(modified_program)
    if terminated:
        print("Part two:", acc)
        break

