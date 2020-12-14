#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Common library for Advent of Code 2020, day 14
"""

class Instruction:
    INVALID = -1
    MASK = 0
    MEMSET = 1


def run(program):
    memory = {}
    active_mask = None
    for instr, fn in program:
        if instr == Instruction.MASK:
            active_mask = fn
        elif instr == Instruction.MEMSET:
            fn(memory, active_mask)
    return sum(memory.values())
