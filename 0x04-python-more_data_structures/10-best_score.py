#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) is 0:
        return None
    name = next(iter(a_dictionary.keys()))
    high = next(iter(a_dictionary.values()))
    for index in a_dictionary.keys():
        if a_dictionary[index] > high:
            high = a_dictionary[index]
            name = index
    return (name)
