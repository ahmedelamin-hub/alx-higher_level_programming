#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if ytr == search else ytr for ytr in my_list]
    return (new_list)
