#!/usr/bin/python3
"""module contains 1 function
        find_peak
"""


def find_peak(list_of_integers):
    """finds a peak in a list of integers"""
    if not list_of_integers:
        return None

    p = list_of_integers[0]

    for pos, i in enumerate(list_of_integers):
        if not isinstance(i, int):
            return None
        if pos not in [0, len(list_of_integers) - 1]:
            if i >= p and \
               list_of_integers[pos - 1] <= i >= list_of_integers[pos + 1]:
                p = i

    return p
