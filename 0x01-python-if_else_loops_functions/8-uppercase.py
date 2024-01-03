#!/usr/bin/python3
def uppercase(str):
    for up in str:
        yes = up
        if ord(yes) >= 97 and ord(yes) <= 122:
            yes = chr(ord(yes) - 32)
        print("{}".format(yes), end="")
        print()
