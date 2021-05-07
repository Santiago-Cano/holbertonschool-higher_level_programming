#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    newdict = {}
    for key in a_dictionary:
        newdict[key] = a_dictionary[key] * 2
    return (newdict)
