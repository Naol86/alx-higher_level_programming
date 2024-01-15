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
    temp.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(sys.argv[4]))
    states = temp.fetchall()
    for state in states:
        print(state)
    temp.close
    db.close()

