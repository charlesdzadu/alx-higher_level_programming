#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    if len(sys.argv) == 1:
        print("0")
    elif len(sys.argv) == 2:
        print("{}".format(sys.argv[1]))
    else:
        for i in range(1, len(sys.argv)):
            sum += int(sys.argv[i])
        print("{}".format(sum))
