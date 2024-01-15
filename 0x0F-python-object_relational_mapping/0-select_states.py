#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
    argv = sys.argv
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    temp = db.cursor()
    temp.execute("SELECT * FROM `states`")
    for i in temp:
        print(i)
