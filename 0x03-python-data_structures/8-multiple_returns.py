#!/usr/bin/python3
def multiple_returns(sentence):
    elmotuple = ()
    if len(sentence) == 0:
        elmotuple = 0, "None"
    else:
        elmotuple = len(sentence), sentence[0]
    return elmotuple
