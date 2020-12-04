#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 04

Run with:

    python3 main.py < input.txt
"""

from collections import defaultdict
from itertools import takewhile
from re import match
from sys import stdin


class IntValidator:
    def __init__(self, minvalue, maxvalue):
        self.minvalue = minvalue
        self.maxvalue = maxvalue
    def __call__(self, value):
        value = int(value)
        return value >= self.minvalue and value <= self.maxvalue


class HeightValidator:
    def __call__(self, value):
        if value.endswith('cm'):
            return IntValidator(150, 193)(value[:-2])
        elif value.endswith('in'):
            return IntValidator(59, 76)(value[:-2])
        return False


class RegexValidator:
    def __init__(self, regex):
        self.regex = regex
    def __call__(self, value):
        return bool(match(self.regex, value))


class CountryIdValidator:
    def __call__(self, value):
        return True


class DefaultValidator:
    def __call__(self, value):
        return False


def fields_exist(passport, required_fields):
    return all(field in passport for field in required_fields)


def valid_passport(passport, required_fields):
    validators = defaultdict(DefaultValidator,
        {
            'byr': IntValidator(1920, 2002),
            'iyr': IntValidator(2010, 2020),
            'eyr': IntValidator(2020, 2030),
            'hgt': HeightValidator(),
            'hcl': RegexValidator(r'^#[0-9a-f]{6}$'),
            'ecl': RegexValidator(r'^(amb|blu|brn|gry|grn|hzl|oth)$'),
            'pid': RegexValidator(r'^\d{9}$'),
            'cid': CountryIdValidator()
        }
    )
    return (fields_exist(passport, required_fields) and
            all(validators[key](val) for key, val in passport.items()))


def passport(data):
    while True:
        yield dict(
            record.split(':')
            for line in takewhile(lambda x: x.strip(), data)
            for record in line.split()
        )


passports = list(takewhile(lambda x: len(x) > 0, passport(stdin)))
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

print("Part one:", sum(1 if fields_exist(pp, required_fields) else 0 for pp in passports))
print("Part two:", sum(1 if valid_passport(pp, required_fields) else 0 for pp in passports))
