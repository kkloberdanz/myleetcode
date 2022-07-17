#!/usr/bin/env python3


import sys


def atoi(s: str) -> int:
    as_int = 0
    zero_value = ord('0')
    s = s.strip()
    if s[0] == '-':
        sign = -1
        s = s[1:]
    else:
        sign = 1

    tens_place = 0
    for c in s[::-1]:
        if ord(c) >= ord('0') and ord(c) <= ord('9'):
            as_int += (ord(c) - zero_value) * 10**tens_place
            tens_place += 1
    return sign * as_int


if __name__ == '__main__':
    for num in sys.argv[1:]:
        print(atoi(num))
