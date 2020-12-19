#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Alternative solution for Advent of Code 2020, day 18 part 2

Usage: python3 alternative.py < input.txt
"""

from re import findall
from sys import stdin


class Parser:
    """
    expression     : multiplication
    multiplication : addition ( "*" addition )*
    addition       : unary ( "+" unary )*
    unary          : int | "(" expression ")"
    """
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        self.current = 0
        return self.expression()

    def peek(self):
        return self.tokens[self.current] if self.current < len(self.tokens) else None

    def take(self):
        self.current = self.current + 1
        return self.tokens[self.current - 1]

    def expression(self):
        return self.multiplication()

    def multiplication(self):
        expr = self.addition()
        while self.peek() == '*':
            self.take()  # "*"
            rhs = self.addition()
            expr = expr * rhs
        return expr

    def addition(self):
        expr = self.unary()
        while self.peek() == '+':
            self.take()  # "+"
            rhs = self.unary()
            expr = expr + rhs
        return expr

    def unary(self):
        if self.peek() == '(':
            self.take()  # "("
            expr = self.expression()
            self.take()  # ")"
            return expr
        return int(self.take())


def tokenize(s):
    return list(findall(r'\d+|[*+()]', s))


def evaluate(expr):
    return Parser(tokenize(expr)).parse()


if __name__ == '__main__':
    print("Part two:", sum(evaluate(line) for line in stdin))
