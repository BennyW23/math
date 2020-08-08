#!/usr/bin/env python3
import math


def spectrum(value, power):
    remainder = value % 1
    ans = math.pow(remainder, power)
    return ans % 1


def test(value):
    print("The spectrum sequence for {} is: ".format(value))
    for i in range(1, 10):
        print(spectrum(value, i), end=", \n")


if __name__ == "__main__":
    test(math.sqrt(2))
