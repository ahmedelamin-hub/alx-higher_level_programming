#!/usr/bin/python3

def fizzbuzz():
    for n in range(1, 101):
        result = ""
        if n % 3 == 0:
            result += "Fizz"
        if n % 5 == 0:
            result += "Buzz"
        print(result if result else "{} ".format(n), end="")

# Check if the script is being run directly


