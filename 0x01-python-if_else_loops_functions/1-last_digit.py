#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = abs(number) % 10
if number < 0:
    last_dig = -(last_dig)
stringis = "Last digit of {} is {}".format(number, last_dig)
if last_dig > 5:
    print(f"{stringis} and is greater than 5")
elif last_dig == 0:
    print(f"{stringis} and is 0")
elif last_dig < 6:
    print(f"{stringis} and is less than 6 and not 0")
