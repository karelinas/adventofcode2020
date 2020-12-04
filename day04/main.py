#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Full solution for Advent of Code 2020, day 04

Run with:

    python3 main.py < input.txt
"""

from sys import stdin
from itertools import takewhile


def fields_exist(passport, required_fields):
    return all(field in passport for field in required_fields)


def valid_int(string, minval, maxval):
    value = int(string)
    return value >= minval and value <= maxval


def valid_height(string):
    if string.endswith('cm'):
        return valid_int(string[:-2], 150, 193)
    elif string.endswith('in'):
        return valid_int(string[:-2], 59, 76)
    return False


def valid_hair_color(string):
    allowed_characters = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                          'a', 'b', 'c', 'd', 'e', 'f')
    return (len(string) == 7 and string[0] == '#' and
            all(ch in allowed_characters for ch in string[1:]))


def valid_eye_color(string):
    return string in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def valid_pid(string):
    allowed_characters = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    return len(string) == 9 and all(ch in allowed_characters for ch in string)


def valid_field(field, value):
    if field == 'byr':
        return valid_int(value, 1920, 2002)
    elif field == 'iyr':
        return valid_int(value, 2010, 2020)
    elif field == 'eyr':
        return valid_int(value, 2020, 2030)
    elif field == 'hgt':
        return valid_height(value)
    elif field == 'hcl':
        return valid_hair_color(value)
    elif field == 'ecl':
        return valid_eye_color(value)
    elif field == 'pid':
        return valid_pid(value)
    elif field == 'cid':
        return True
    return False


def valid_passport(passport, required_fields):
    return (fields_exist(passport, required_fields) and
            all(valid_field(key, val) for key, val in passport.items()))


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
