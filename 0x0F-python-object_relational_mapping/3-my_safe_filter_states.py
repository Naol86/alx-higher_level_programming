#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
    argv = sys.argv
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1], password=argv[2], db=argv[3])
    temp = db.cursor()
    temp.execute("SELECT * FROM states WHERE name LIKE %s",(sys.argv[4],))
    states = temp.fetchall()
    for state in states:
        print(state)
