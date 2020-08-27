#!/usr/bin/env python3
"""
    Usage:

    This file counts the number of ways of pairing up n elements where not every element has to be paired.
    It translates to finding the number of elements a in Sn such that a^2 = 1
    where Sn is the symmetric group of order n
"""

import itertools

cache = {}  # for recursive implementation

"""
Brute force search of generating all sets of pairings and then counting them, abusing sets to remove duplicates
"""


def brute_force(n):
    all_pairs = set()
    for permutation in itertools.permutations(range(1, n + 1)):
        for num_paired_elements in range(2, n + 1, 2):
            pairs = set()
            for i in range(0, num_paired_elements, 2):
                minimum = min(permutation[i], permutation[i + 1])
                maximum = max(permutation[i], permutation[i + 1])
                pairs.add((minimum, maximum))

            all_pairs.add(tuple(sorted(pairs)))
    all_pairs.add(())
    for pair in sorted(all_pairs):
        print(pair)
    return len(all_pairs)


"""
Try to calculate it explicitly, considering the number of permutations
We look at "batches" of sizes that are multiples of 2
e.g suppose we consider permutations of size 6 = 3 * 2, which describes three pairs.
    Since we care about combinations, order between the pairs and order within the pairs doesn't matter
    so we divide by 2^3 because we have 3 pairs, and 3! because that's the number of ways we can order the pairs
"""


def calculate(n):
    total = 0
    for i in range(0, (n // 2) + 1):
        permutations = num_permutations(n, 2 * i)
        pairs = permutations / (2 ** i)
        pairs = pairs / num_permutations(i, i)  # weird way of doing a factorial
        # print ((i, pairs))
        total += pairs
    return total


def num_permutations(n, r):
    product = 1
    for i in range(r):
        product *= n - i
    return product


"""
turns out theres an easier way
"""


def recursive(n):
    global cache
    if n < 2:
        return 1
    if n == 2:
        return 2
    if not n in cache:
        cache[n] = (n - 1) * recursive(n - 2) + recursive(n - 1)
    return cache[n]


def test():
    pass


if __name__ == "__main__":
    # n = 9
    # print(brute_force(n))
    for n in range(20):
        print("n = {}".format(n))
        print(calculate(n))
        print(recursive(n))
        print()
