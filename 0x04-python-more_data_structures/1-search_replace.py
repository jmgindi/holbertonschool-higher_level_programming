#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for index, element in enumerate(my_list):
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)

    return new_list
