#!/usr/bin/env python3

import sys


def validate(stmt):
    toks = []
    openers = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    closers = set(openers.values())
    for c in stmt:
        if c in openers:
            toks.append(c)
        elif c in closers:
            if toks:
                matching = toks.pop()
                if c != openers[matching]:
                    print(f"{c} does not match with {matching}")
                    return False
            else:
                print(f"unmatched token: {c}")
                return False
        else:
            print(f"invalid token: {c}")
            return False

    if toks:
        print("did not consume all tokens")
        return False
    return True


if __name__ == "__main__":
    for paren in sys.argv[1:]:
        if validate(paren):
            print(paren, "VALID")
        else:
            print(paren, "INVALID")
