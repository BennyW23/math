#!/usr/bin/env python3
"""
    Usage:

    This file contains code to generate the Farey series of order n
"""
from fractions import Fraction
import math


def farey(order):
    values = []
    for n in range(1, order + 1):
        for m in range(n):
            if math.gcd(n, m) == 1:
                values.append(Fraction(m, n))
    values.append(Fraction(1, 1))
    return sorted(values)


def display(order):
    values = farey(order)
    print("The Farey Series of order {} is: ".format(order))
    for frac in values:
        print("{}/{}".format(frac.numerator, frac.denominator))


if __name__ == "__main__":
    display(4)
