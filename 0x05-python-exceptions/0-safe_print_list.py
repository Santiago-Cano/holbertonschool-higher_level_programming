#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while i in range(0, x):
        try:
            print("{}".format(my_list[i]), end='')
        except IndexError:
            break
        i = i + 1
    print("")
    return(i)
