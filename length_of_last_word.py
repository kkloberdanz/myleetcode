#!/usr/bin/env python3

import sys


def lenth_of_last_word(stmt):
    words = stmt.split()
    return len(words[-1])


if __name__ == "__main__":
    for stmt in sys.argv[1:]:
        print(stmt, lenth_of_last_word(stmt))
