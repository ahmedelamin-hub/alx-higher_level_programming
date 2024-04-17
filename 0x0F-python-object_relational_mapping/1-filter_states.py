#!/usr/bin/python3
"""
A script that lists all states with names starting with 'N' from the
database 'hbtn_0e_0_usa'.
"""

import MySQLdb
import sys

def filter_states(username, password, dbname):
    """
    Connects to a MySQL database and prints states starting with 'N'.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
