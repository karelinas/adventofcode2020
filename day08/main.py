#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 08

Usage:

    python3 main.py < input.txt
"""

from collections import namedtuple
from re import match
from sys import stdin

Instruction = namedtuple('Instruction', ['op', 'arg'])

class Cpu:
    instructions = {
        'nop': lambda pc, acc, arg: (pc+1, acc),
        'acc': lambda pc, acc, arg: (pc+1, acc+arg),
        'jmp': lambda pc, acc, arg: (pc+arg, acc)
    }

    @classmethod
    def run(cls, program):
        pc, acc = 0, 0
        seen = set()
        while pc < len(program) and pc not in seen:
            seen.add(pc)
            pc, acc = cls.instructions[program[pc].op](pc, acc, program[pc].arg)
        return (pc not in seen, acc)


def instruction(line):
    op, arg = match(r'^(\w+) ([+-]*\d+)$', line).groups()
    return Instruction(op, int(arg))


def swap_operator(ops, pos):
    swap_map = {
        'jmp': 'nop',
        'nop': 'jmp',
        'acc': 'acc'
    }
    return ops[:pos] + [Instruction(swap_map[ops[pos].op], ops[pos].arg)] + ops[pos+1:]


program = [instruction(line) for line in stdin]

terminated, acc = Cpu.run(program)
print("Part one:", acc)

for i in range(len(program)):
    fix_candidate = swap_operator(program, i)
    terminated, acc = Cpu.run(fix_candidate)
    if terminated:
        print("Part two:", acc)
        break
