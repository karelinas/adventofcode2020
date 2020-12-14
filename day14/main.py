#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main program for Advent of Code 2020, day 14

Usage:

    python3 main.py < input.txt
"""

from sys import stdin

from common import Instruction, run
import partone
import parttwo

raw_program = list(map(str, stdin))

print("Part one:", run(map(partone.instruction, raw_program)))
print("Part two:", run(map(parttwo.instruction, raw_program)))
