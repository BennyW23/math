#!/usr/bin/env python3
"""
    Usage:
    Result:

    Modular arithmetic calculator based on Problem 0.3.16 of Dummit and Foote's Abstract Algebra
"""
import sys


def mod(value, modulus):
    """
        mod(int, int) -> int

        Finds the least non-negative representative of the group
        of value given, with respect to the modulus
    """
    quotient = value // modulus
    return value - quotient * modulus


def add(value1, value2, modulus):
    """
        add(int, int, int) -> int

        Adds the two values and returns the sum, mod modulus
    """
    value1 = mod(value1, modulus)
    value2 = mod(value2, modulus)
    total = value1 + value2
    return mod(total, modulus)


def multiply(value1, value2, modulus):
    """
        multiply(int, int, int) -> int

        Multiplies the two values and returns the product, mod modulus
    """
    value1 = mod(value1, modulus)
    value2 = mod(value2, modulus)
    product = value1 * value2
    return mod(product, modulus)


def gcd(value1, value2):
    """
        gcd(int,int) -> int

        Finds the greatest common denominator of two numbers
        Uses the Euclidean algorithm
    """
    if value1 == 0 or value2 == 0:
        return 0

    # gcd(a,b) = gcd(|a|,|b|)
    value1 = abs(value1)
    value2 = abs(value2)

    # let |value1| >= |value2|
    temp = min(value1, value2)
    value1 = max(value1, value2)
    value2 = temp

    while temp != 0:
        temp = mod(value1, value2)
        value1 = value2
        value2 = temp
    return value1


def inverse(value, modulus):
    """
        inverse(int, int) -> int OR None

        If gcd(value, modulus) = 1
            Find the multiplicative inverse such that:
            value * inverse = 1 mod modulus
            using the Extended Euclidean Algorithm
        Otherwise returns None
    """
    rows = []
    rows.append((value, 1))
    rows.append((modulus, 0))

    while True:
        # compare the two most recent rows of the list
        if rows[-1][0] == 0:
            break
        quotient = rows[-2][0] // rows[-1][0]
        new_total = mod(rows[-2][0], rows[-1][0])
        new_elem = rows[-2][1] - quotient * rows[-1][1]
        rows.append((new_total, new_elem))

    if rows[-2][0] == 1:
        return mod(rows[-2][1], modulus)
    return None


def main():
    """
        main method to run program
    """
    arguments = sys.argv
    while len(arguments) < 4:
        arguments.append(None)

    modulus = get_value("modulus", arguments[1], True)
    value1 = get_value("value1", arguments[2], False)
    value2 = get_value("value2", arguments[3], False)
    calculate(value1, value2, modulus)


def get_value(name, default, positive_only):
    """
        get_value(string, int, boolean) -> int

        Returns an int representing the value of string.
        String is used for prompting the user what to enter.
    """

    if default is not None:
        value = default
    else:
        print("Please enter a value for {}:".format(name))
        value = input()

    while True:
        try:
            value = int(value)
            if positive_only:
                if value < 0:
                    value *= -1
                elif value == 0:
                    raise ArithmeticError("Tried to use a value of 0")
            break
        except (ValueError, ArithmeticError):
            print(
                "Invalid number! Please enter an integer to use as the {}:".format(name)
            )
            value = input()
    return value


def test():
    """
        Test cases in the form of (value1, value2, modulus)
        When run, does calculations on all of them and prints all results
    """
    test_cases = [
        (0, 1, 3),
        (3, 3, 4),
        (2, 3, 4),
        (4, 3, 4),
        (120, 150, 4),
        (121, 2, 42),
        (2, -6, -10),
        (80, 80, 62),
        (35, 60, 17),
        (35, 17, 60),
    ]
    for case in test_cases:
        calculate(*case)


def calculate(value1, value2, modulus):
    """
        calculate(int, int, int)

        Calls the calculations defined in the program and calls them.
    """
    print()
    print()
    print(
        "{} + {} = {} mod {}".format(
            value1, value2, add(value1, value2, modulus), modulus
        )
    )
    print(
        "{} x {} = {} mod {}".format(
            value1, value2, multiply(value1, value2, modulus), modulus
        )
    )
    if inverse(value1, modulus) is not None:
        print(
            "The inverse of {} mod {} is {}".format(
                value1, modulus, inverse(value1, modulus)
            )
        )
    else:
        print(
            "The GCD is {} and {} is {}, so no inverse exists".format(
                value1, modulus, gcd(value1, modulus)
            )
        )
    if inverse(value2, modulus) is not None:
        print(
            "The inverse of {} mod {} is {}".format(
                value2, modulus, inverse(value2, modulus)
            )
        )
    else:
        print(
            "The GCD of {} and {} is {}, so no inverse exists".format(
                value2, modulus, gcd(value2, modulus)
            )
        )


if __name__ == "__main__":
    # main()
    test()
