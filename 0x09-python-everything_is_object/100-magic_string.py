#!/usr/bin/python3
'''defines class'''


def magic_string():
    '''magic string'''
    
    magic_string.counter = getattr(magic_string, 'counter', 0) + 1
    return "BestSchool, " * (magic_string.counter - 1) + "BestSchool"
