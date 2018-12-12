#!/usr/bin/python3
def max_integer(my_list=[]):
    a = my_list[0]
    for i in range(len(my_list)):
        if a < my_list[i]:
            a = my_list[i]
    return a
