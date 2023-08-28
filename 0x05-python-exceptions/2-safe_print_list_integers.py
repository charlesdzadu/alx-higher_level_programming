#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    printed_ints = 0
    while True:
        try:
            if i < x:
                print("{:d}".format(my_list[i]), end='')
                i += 1
                printed_ints += 1
            else:
                print()
                return printed_ints
        except (ValueError, TypeError):
            i += 1
