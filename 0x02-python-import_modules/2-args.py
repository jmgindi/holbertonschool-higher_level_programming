#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    largv = len(argv) - 1
    if largv == 0:
        print("0 arguments.")
    elif largv == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(largv))

    if largv >= 1:
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
            i += 1
    else:
        pass
