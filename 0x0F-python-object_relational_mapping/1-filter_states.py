#!/usr/bin/python3

"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./1-filter_state.py <mysql username> \
                            <mysql password> \
                            <database name>
"""

import sys
import MySQLdb

if __name__ == '__main__':
    argv = sys.argv
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    temp = db.cursor()
    temp.execute("SELECT * FROM `states`")
    for i in temp:
        if i[1][0] == 'N':
            print(i)
