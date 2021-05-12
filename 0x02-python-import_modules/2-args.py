#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)

    if i == 2:
        print("1 argument:")
    elif i == 1:
        print("0 arguments:")
    elif i > 2:
        print("{} arguments:".format(i - 1))
    for x in range(1, i):
        print("{}: {}".format(x, sys.argv[x]))
