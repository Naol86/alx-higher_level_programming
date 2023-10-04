#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last = abs(number) % 10
last = last if number > 0 else -last
info = "0"
if last > 5:
    info = "greater than 5"
elif last != 0:
    info = "less than 6 and not 0"
print(f"Last digit of {number} is {last} and is {info}")
