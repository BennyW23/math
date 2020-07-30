#!/usr/bin/env python3
import sys
import math

if (len(sys.argv) != 3):
    print("Usage: logistic_map.py {r_value} {x_0}")
    exit(0);

r = float(sys.argv[1])
x = float(sys.argv[2])
iterate = 0

print("Executing with r value {} and initial condition {}".format(r,x))

while True:
    print("Iterate {}, x_n = {}".format(iterate,x))
    x = r * x * (1.0 - x)
    iterate += 1
