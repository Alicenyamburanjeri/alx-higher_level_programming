#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa:
 script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
use the module MySQLdb (import MySQLdb)
Results must be sorted in ascending order by states.id
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    rows = cur.fetchall()
    for row in rows:
        print(row)
