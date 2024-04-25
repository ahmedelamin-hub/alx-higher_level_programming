#!/usr/bin/python3
"""
Module 6-peak contains a function
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    A peak element is one that is not smaller than

    Args:
        list_of_integers (list): The list of integers.

    Returns:
        int: A peak element, or None if it cannot be found.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1
    while low <= high:
        mid = (low + high) // 2
        # Check if current element is a peak
        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return None
