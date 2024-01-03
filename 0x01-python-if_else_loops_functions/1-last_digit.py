#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = abs(number) % 10
mess = f"Last digit of {number} is {last_dig} and is"
if last_dig > 5:
    mess += "greater than 5"
elif last_dig == 0:
    mess += "0"
else:
    mess += "less than 6 and not 0"
print(mess)
