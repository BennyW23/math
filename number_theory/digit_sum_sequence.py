#!/usr/bin/env python3
"""
    This file is just to test out something I thought of.
    What's the sequence created from adding the sum of the digits of the number to the number?
"""


def iterate(n, start=1):
    value = start
    for iter in range(n):
        print(value, end=", ")
        value += digit_sum(value)


def digit_sum(n):
    num_string = str(n)
    total = 0
    for digit in num_string:
        total += int(digit)
    return total


def test():
    pass


if __name__ == "__main__":
    iterate(50, start=1)
