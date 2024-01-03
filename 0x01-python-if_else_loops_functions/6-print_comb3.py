#!/usr/bin/python3
for play in range(0, 10):
    for hed in range(play + 1, 10):
        if play == 8 and hed == 9:
            print('89')
        else:
            print('{}{}, '.format(play, hed), end="")
