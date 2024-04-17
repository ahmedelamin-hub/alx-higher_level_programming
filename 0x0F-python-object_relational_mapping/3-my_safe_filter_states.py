#!/usr/bin/python3
"""
A script that takes in arguments and displays all values in the 'states' table
of the database 'hbtn_0e_0_usa' where the name matches the argument provided.
This version is safe from MySQL injections.
"""

import MySQLdb
import sys


def safe_fetch_states(username, password, dbname, search_name):
    """
    Fetches states from the database using safe methods to prevent
    SQL injection.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (search_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        safe_fetch_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
