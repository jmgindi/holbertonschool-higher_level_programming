#!/usr/bin/python3
for a in range(ord('a'), (ord('z') + 1)):
    if a not in [ord('e'), ord('q')]:
        print("{}".format(chr(a)), end = "")
