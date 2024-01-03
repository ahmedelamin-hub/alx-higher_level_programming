#!/usr/bin/python3

def fizzbuzz():
    for number in range(1, 101):
        result = ""
        if number % 3 == 0:
            result += "Fizz"
        if number % 5 == 0:
            result += "Buzz"
        print(result if result else "{} ".format(number), end="")

# Call the function to execute FizzBuzz
fizzbuzz()

