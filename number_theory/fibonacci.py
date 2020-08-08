#!/usr/bin/env python3
"""
This file will contain ways of computing the nth fibonacci number
"""
import functools
import time
import math
import sys

cache = {}


def fibonacci(n):
    return fibonacci_recursive_cache(n)


def fibonacci_direct(n):
    """
    accurate until 308061521170129 based on testing here... interesting
    """
    phi = (1 + math.sqrt(5)) / 2
    return round((math.pow(phi, n) / math.sqrt(5)))


def fibonacci_recursive_cache(n):
    """
    Uses memoization to compute the nth fibonacci number
    :param n:  non-negative integer representing the index desired
    :return: the nth fibonacci number
    """
    global cache

    if n < 2:
        return 1
    if not n in cache:
        cache[n] = fibonacci_recursive_cache(n - 2) + fibonacci_recursive_cache(n - 1)
    return cache[n]


@functools.lru_cache(None)
def fibonacci_recursive_functools(n):
    """
    Uses functools lru_cache to compute the nth fibonacci number
    very heavy on memory apparently, stack overflows before the memoized version
    :param n:  non-negative integer representing the index desired
    :return: the nth fibonacci number
    """
    if n < 2:
        return 1
    return fibonacci_recursive_functools(n - 1) + fibonacci_recursive_functools(n - 2)


def test(n):
    functions = [
        "fibonacci_direct",
        "fibonacci_recursive_cache",
        "fibonacci_recursive_functools",
    ]
    results = []
    for function_name in functions:
        function = globals()[function_name]
        print("{} is finding the first {} fibonacci numbers".format(function_name, n))
        start = time.perf_counter()
        for i in range(0, n):
            function(n)
        end = time.perf_counter()
        result_string = "{} took {} to find the first {} fibonacci numbers".format(
            function_name, end - start, n
        )
        print(result_string)
        results.append(result_string)

    print()
    print("Final Results:")
    for result in results:
        print(result)


if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    test(1000)
