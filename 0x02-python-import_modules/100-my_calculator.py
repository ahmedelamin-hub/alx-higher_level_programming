#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

        a, op, b = int(argv[1]), argv[2], int(argv[3])

        if op == "+":
            re = a + b
        elif op == "-":
            re = a - b
        elif op == "*":
            re = a * b
        elif op == "/":
            re = a / b
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

        print("{} {} {} = {}".format(a, op, b, re)
        exit(0)
