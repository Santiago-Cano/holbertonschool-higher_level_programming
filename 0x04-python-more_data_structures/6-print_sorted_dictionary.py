#!/usr/bin
def print_sorted_dictionary(a_dictionary):
    for index in sorted(a_dictionary):
        print("{}: {}".format(index, a_dictionary[index]))
