#!/usr/bin/python3
for a in range(122, 96, -1):
    print("{}".format(chr(a - 32) if a % 2 else chr(a)), end="")
