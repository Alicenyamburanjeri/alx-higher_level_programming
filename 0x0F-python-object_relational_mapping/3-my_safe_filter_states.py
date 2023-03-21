#!/usr/bin/python3
"""
A script that  takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument and is safe from MySQL injections!
Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
"""

import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s;", (sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    cur.close()
    db.close()
