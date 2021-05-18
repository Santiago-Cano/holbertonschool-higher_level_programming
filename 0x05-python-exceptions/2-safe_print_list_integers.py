#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    while i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except IndexError:
            break
        except ValueError, TypeError:
            pass
        i = i + 1
    return (i)
