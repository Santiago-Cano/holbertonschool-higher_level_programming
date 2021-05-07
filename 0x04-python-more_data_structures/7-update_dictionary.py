#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None:
        return None
    dicappend = {key: value}
    a_dictionary.update(dicappend)
    return(a_dictionary)
