#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *

    fl = dir()
    for x in range(0, len(fl)):
        if fl[x][:2] != "__":
            print("{:s}".format(fl[x]))
