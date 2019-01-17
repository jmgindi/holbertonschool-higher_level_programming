#!/usr/bin/python3
"""
Module contains one class:
    MyList
"""

class MyList(list):
    def print_sorted(self):
        sl = [i for i in self]
        sl.sort()
        print(sl)
