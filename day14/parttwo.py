#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Library for Advent of Code 2020, day 14 part 2
"""

from functools import reduce
from itertools import product
from re import match

from common import Instruction

def mask(maskstr):
    def maskstr_replace(maskstr, xlist):
        return reduce(lambda s, x: s.replace('X', x, 1), xlist, maskstr)

    def resolve(addr):
        xcount = maskstr.count('X')
        addr = ''.join([a if x == '0' else x for a, x in zip(bin(addr)[2:].zfill(len(maskstr)), maskstr)])
        return [int(maskstr_replace(addr, xs), 2) for xs in product(['0', '1'], repeat=xcount)]

    return resolve

def memset(addr, val):
    def apply_memset(mem, mask):
        for a in mask(addr):
            mem[a] = val
    return apply_memset

def instruction(line):
    mo = match(r'^mask = ([01X]+)$', line)
    if mo:
        return (Instruction.MASK, mask(mo.group(1)))
    mo = match(r'^mem\[(\d+)\] = (\d+)$', line)
    if mo:
        return (Instruction.MEMSET, memset(int(mo.group(1)), int(mo.group(2))))
    return (INVALID, None)
