#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    args = "arguments" if argc != 1 else "argument"
    print("{} {}{}{}".format(argc, args, ":" if argc != 0 else ".", ""))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, argv[i]))

