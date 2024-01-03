#!/usr/bin/python3
for x in range(ord('z'), ord('a')- 1, -1):
    if x % 2 == 0:
        change = 0
    else:
        change = 32
    print('{}'.format(chr(x - change)), end="")
