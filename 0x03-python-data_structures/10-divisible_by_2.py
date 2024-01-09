#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    liv = []
    for we in range(len(my_list)):
        if my_list[we] % 2 == 0:
            liv.append(True)
        else:
            liv.append(False)
    return liv
