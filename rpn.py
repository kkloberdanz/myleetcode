#!/usr/bin/env python3


import sys

ops = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


def eval_op(op, a, b):
    return ops[op](b, a)


def token_to_num(tok):
    try:
        return int(tok)
    except Exception:
        return float(tok)


def token_is_digit(tok):
    try:
        token_to_num(tok)
        return True
    except Exception:
        return False


def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token_is_digit(token):
            stack.append(token)
        else:
            a = token_to_num(stack.pop())
            b = token_to_num(stack.pop())
            c = eval_op(token, a, b)
            stack.append(c)
    return int(stack.pop())


if __name__ == "__main__":
    print(eval_rpn(sys.argv[1].split()))
