#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 02

Usage:

    python3 main.py < input.txt
"""

import re
from sys import stdin


class PreviousEmployerValidator:
    @staticmethod
    def __call__(password, policy):
        count = password.count(policy.get('character'))
        return count >= policy.get('n1') and count <= policy.get('n2')


class TobogganCorporateValidator:
    @staticmethod
    def __call__(password, policy):
        character = policy.get('character')
        idx1 = policy.get('n1') - 1
        idx2 = policy.get('n2') - 1
        return (password[idx1] == character) ^ (password[idx2] == character)


def valid_count(data, validator):
    return [validator(password, policy) for password, policy in data].count(True)


def parsed_data(raw_data):
    mo = re.match(r'^(\d+)-(\d+) (\w): (\w+)$', raw_data)
    assert mo, "Invalid input data"
    password = mo.group(4)
    policy = {
        'character': mo.group(3),
        'n1': int(mo.group(1)),
        'n2': int(mo.group(2))
    }
    return password, policy


data = [parsed_data(line) for line in stdin]
print("Part one:", valid_count(data, PreviousEmployerValidator()))
print("Part two:", valid_count(data, TobogganCorporateValidator()))
