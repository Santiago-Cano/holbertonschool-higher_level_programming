#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return ([replace if index == search else index for index in my_list])
