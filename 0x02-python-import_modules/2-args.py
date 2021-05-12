#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1

    if i == 1:
        print("1 argument:")
    elif i == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(i))
    for x in range(1, i + 1):
        print("{}: {}".format(x, sys.argv[x]))
