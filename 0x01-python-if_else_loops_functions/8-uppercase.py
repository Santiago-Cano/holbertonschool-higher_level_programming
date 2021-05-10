#!/usr/bin/python3
def uppercase(str):
    for index in str:
        if index.islower():
            index = chr(ord(index) - ord(' '))
        print("{}".format(index), end='')
    print()
