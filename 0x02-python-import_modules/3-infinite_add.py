#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    gc = len(argv) - 1
    result = 0

    for pop in range(1, gc + 1):
        result += int(argv[pop])

    print(result)
