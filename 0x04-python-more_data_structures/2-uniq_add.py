#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqs = []
    sum = 0
    for i in my_list:
        if i not in uniqs:
            sum += i
            uniqs.append(i)

    return sum
