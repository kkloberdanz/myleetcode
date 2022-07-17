#!/usr/bin/env python3


import sys


def _atoi(s: str) -> int:
    as_int = 0
    zero_value = ord('0')
    s = s.strip()
    if s[:2] == '+-' or s[:2] == '-+':
        return 0

    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        sign = 1
        s = s[1:]
    else:
        sign = 1

    tens_place = 0
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    for c in s[::-1]:
        if c == '.':
            as_int = 0
            tens_place = 0
        elif ord(c) >= ord('0') and ord(c) <= ord('9'):
            as_int += (ord(c) - zero_value) * 10**tens_place
            if sign * as_int > INT_MAX:
                return INT_MAX
            if sign * as_int < INT_MIN:
                return INT_MIN
            tens_place += 1
        else:
            return 0
    return sign * as_int


def atoi(s: str) -> int:
    words = s.split()
    if words:
        return _atoi(words[0])
    else:
        return 0

if __name__ == '__main__':
    for num in sys.argv[1:]:
        print(atoi(num))
