#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    name = "hi"
    high = 0
    for index in a_dictionary:
        if a_dictionary[index] > high:
            high = a_dictionary[index]
            name = index
    return (name)
