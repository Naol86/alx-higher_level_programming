#!/usr/bin/python3

n = 97
for i in range(26):
    if i == 4 or i == 16:
        continue
    print(chr(n+i), end="")
