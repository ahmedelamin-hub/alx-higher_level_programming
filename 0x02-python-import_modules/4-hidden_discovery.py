#!/usr/bin/python3
if __name__ == " __main__":
    from hidden_4 import *
    tobe = dir()
    for x in range(0, len(tobe)):
        if tobe[x][:2] != "__":
            print("{:s}".format(tobe[x]))
