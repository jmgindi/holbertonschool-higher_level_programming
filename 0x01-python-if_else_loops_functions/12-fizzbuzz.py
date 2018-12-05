#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            n = "FizzBuzz"
        elif i % 5 == 0:
            n = "Buzz"
        elif i % 3 == 0:
            n = "Fizz"
        else:
            n = i
        print("{} ".format(n), end="")
