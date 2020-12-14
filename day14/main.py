#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 14

Usage:

    python3 main.py < input.txt
"""

from itertools import product
from re import match
from sys import stdin


class Instruction:
    INVALID = -1
    MASK = 0
    MEMSET = 1


class Common:
    @classmethod
    def instruction(cls, line):
        mo = match(r'^mask = ([01X]+)$', line)
        if mo:
            return (Instruction.MASK, cls.mask(mo.group(1)))
        mo = match(r'^mem\[(\d+)\] = (\d+)$', line)
        if mo:
            return (Instruction.MEMSET, cls.memset(int(mo.group(1)), int(mo.group(2))))
        return (Instruction.INVALID, None)


class PartOne(Common):
    @staticmethod
    def mask(maskstr):
        def apply_mask(data):
            ormask = int(maskstr.replace('X', '0'), 2)
            andmask = int(maskstr.replace('X', '1'), 2)
            return data & andmask | ormask

        return apply_mask

    @staticmethod
    def memset(addr, val):
        def apply_memset(mem, mask):
            mem[addr] = mask(val)
        return apply_memset


class PartTwo(Common):
    @staticmethod
    def mask(maskstr):
        def replace_xs(s, xlist):
            for x in xlist:
                s = s.replace('X', x, 1)
            return s

        def resolve_addresses(addr):
            binary_addr = bin(addr)[2:].zfill(len(maskstr))
            addr = ''.join(a if x == '0' else x for a, x in zip(binary_addr, maskstr))
            return [int(replace_xs(addr, xs), 2)
                    for xs in product(['0', '1'], repeat=maskstr.count('X'))]

        return resolve_addresses

    @staticmethod
    def memset(addr, val):
        def apply_memset(mem, mask):
            for a in mask(addr):
                mem[a] = val
        return apply_memset


def run(program):
    memory = {}
    active_mask = None
    for instr, fn in program:
        if instr == Instruction.MASK:
            active_mask = fn
        elif instr == Instruction.MEMSET:
            fn(memory, active_mask)
    return sum(memory.values())


raw_program = list(map(str, stdin))

print("Part one:", run(map(PartOne.instruction, raw_program)))
print("Part two:", run(map(PartTwo.instruction, raw_program)))
