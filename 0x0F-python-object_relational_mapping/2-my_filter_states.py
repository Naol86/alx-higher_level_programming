#!/usr/bin/python3

"""
    check if user input is exist in our database
"""

import sys
import MySQLdb

if __name__ == '__main__':
    argv = sys.argv
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    temp = db.cursor()
    temp.execute(f"SELECT * FROM `states` WHERE `name` = \"{argv[4]}\"")
    for i in temp:
        print(i)
