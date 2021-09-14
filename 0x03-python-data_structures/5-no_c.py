#!/usr/bin/python3
def no_c(my_string):
    newstring = list(my_string)
    j = 0
    for i in my_string:
        if i in "cC":
            newstring[j] = ""
        j += 1
    return "".join(newstring)
