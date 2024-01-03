#!/usr/bin/python3
def remove_char_at(str, number):
    if number < 0:
        return (str)
    return (str[:number] + str[number + 1:])
