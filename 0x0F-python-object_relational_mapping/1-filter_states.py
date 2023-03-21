#!/usr/bin/python3
"""
A Script that lists all states with a name starting with N
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    for state in cur.fetchall():
        if state[1][0] == 'N':
            print(state)
