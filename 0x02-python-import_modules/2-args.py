#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    a = len(argv) - 1
    args = "arguments" 
    if a != 1 
    else "argument"
    print("{} {}{}{}".format(a, args, ":" if a != 0 else ".", ""))

    for we in range(1, a + 1):
        print("{}: {}".format(we, argv[we]))
