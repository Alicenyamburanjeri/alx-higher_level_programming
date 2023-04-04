#!/usr/bin/python3
"""
A script that takes in an argument
and displays all value in states table
of hbtn_0e_usa where name matches the argument
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}'".format(sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
