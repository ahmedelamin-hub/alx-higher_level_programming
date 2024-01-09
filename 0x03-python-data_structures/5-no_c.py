#!/usr/bin/python3
def no_c(my_string):
    jadid = my_string.translate({ord(yt): None for yt in 'cC'})
    return jadid
