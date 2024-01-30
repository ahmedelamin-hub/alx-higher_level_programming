#!/usr/bin/python3
"""Defines a txt function."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Parameters:
    text (str): The text to be printed.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1  # Skip any whitespace following the punctuation.
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
