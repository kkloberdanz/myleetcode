#!/usr/bin/env python3


import sys


def gen_parens(n):
    if n == 0:
        yield ""
    for c in range(n):
        for left in gen_parens(c):
            for right in gen_parens(n - 1 - c):
                yield "({}){}".format(left, right)


if __name__ == "__main__":
    for n in sys.argv[1:]:
        for paren in gen_parens(int(n)):
            print(paren)
