#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Library for Advent of Code 2020, day 14 part 1
"""

from re import match
from common import Instruction

def mask(maskstr):
    def apply_mask(data):
        ormask = int(maskstr.replace('X', '0'), 2)
        andmask = int(maskstr.replace('X', '1'), 2)
        return data & andmask | ormask

    return apply_mask

def memset(addr, val):
    def apply_memset(mem, mask):
        mem[addr] = mask(val)
    return apply_memset

def instruction(line):
    mo = match(r'^mask = ([01X]+)$', line)
    if mo:
        return (Instruction.MASK, mask(mo.group(1)))
    mo = match(r'^mem\[(\d+)\] = (\d+)$', line)
    if mo:
        return (Instruction.MEMSET, memset(int(mo.group(1)), int(mo.group(2))))
    return (INVALID, None)
