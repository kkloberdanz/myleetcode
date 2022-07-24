#!/usr/bin/env python3


import sys


def square(x):
    return x * x


def mysqrt(x):
    if x < 2:
        return x

    x0 = x
    x1 = x0 - ((square(x0) - x) / (2 * x0))
    while abs(x0 - x1) >= 1:
        x0 = x1
        x1 = x0 - ((square(x0) - x) / (2 * x0))
    return int(x1)


if __name__ == "__main__":
    for n in sys.argv[1:]:
        ans = mysqrt(int(n))
        print(f"sqrt({n}) = {ans}")
