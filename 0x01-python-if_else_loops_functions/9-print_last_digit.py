#!/usr/python3
def print_last_digit(number):
    if number < 0:
        number = -(number)
    else:
        pass

    l = number % 10
    print("{}".format(l), end="")
    return(l)
