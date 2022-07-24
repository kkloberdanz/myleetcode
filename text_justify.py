#!/usr/bin/env python3


import argparse
import sys


def fill_spaces(line, max_width):
    # place spaces in-between words to get them to file a line
    number_of_words = len(line)
    if number_of_words == 1:
        word = line[0]
        gap_length = max_width - len(word)
        line_string = line[0] + gap_length * " "
    else:
        letter_length = sum(len(word) for word in line)
        gap_length = (max_width - letter_length) // (number_of_words - 1)
        gap_remainder = (max_width - letter_length) % (number_of_words - 1)
        line_string = ""

        # first one needs the remainder
        for i in range(len(line) - 1):
            word = line[i]
            if gap_remainder > 0:
                line_string += word + " " + (gap_length * " ")
            else:
                line_string += word + (gap_length * " ")
            gap_remainder = max(gap_remainder - 1, 0)
        line_string += line[number_of_words - 1]
    return line_string


def justify(words, max_width):
    line_len = 0
    lines = []
    line = []
    i = 0
    num_words = len(words)
    while True:
        if i >= num_words:
            break
        word = words[i]
        word_len = len(word)
        if line_len + word_len <= max_width:
            line_len += word_len + 1
            line.append(word)
            i += 1  # get next word
        else:
            if not line:
                print(
                    f"{sys.argv[0]}: word: '{word}' is too long for {max_width} characters (it is {len(word)} characters long)",
                    file=sys.stderr,
                )
                sys.exit(1)
            lines.append(fill_spaces(line, max_width))
            line = []
            line_len = 0
    if line:
        final_line = " ".join(line)
        gap_length = max_width - len(final_line)
        lines.append(final_line + (" " * gap_length))
    return lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--col", type=int, default=79)
    args = parser.parse_args()
    words = sys.stdin.read().split()
    max_width = args.col
    for line in justify(words, max_width):
        print(line)

# words = ["This", "is", "an", "example", "of", "text", "justification."]
# max_width = 16
# words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
# max_width = 20
# for line in justify(words, max_width):
#    print(f'"{line}"')
