#!/usr/bin/env python3


import copy


def plus_one(digits):
    n = len(digits)
    for i in range(n):
        idx = n - 1 - i
        if digits[idx] == 9:
            digits[idx] = 0
        else:
            digits[idx] += 1
            return digits
    return [1] + digits


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [1, 2, 9],
        [9, 9],
        [8, 9, 9],
        [9, 8, 9],
    ]
    for (ans, test_case) in zip(
        map(lambda x: plus_one(copy.deepcopy(x)), test_cases), test_cases
    ):
        print(test_case, "=>", ans)
