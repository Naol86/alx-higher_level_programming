#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    Len = len(sys.argv) - 1
    if Len == 0:
        print("0 arguments.")
    elif Len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(Len))
    for i in range(Len):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
