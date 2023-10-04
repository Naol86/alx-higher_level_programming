#!/usr/bin/python3

for i in range(100):
    if i < 12:
        print("%.2u" % i, end=', ')
        continue
    if ((i % 10) * 10 + i // 10) > i:
        print(i, end='')
        if i != 99:
            print(", ", end='')
