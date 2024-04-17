#!/usr/bin/python3
"""
A script that displays all values in the 'states' table of the database
'hbtn_0e_0_usa' where name matches the argument provided.
"""

import MySQLdb
import sys


def fetch_states(username, password, dbname, state_name):
    """
    Fetches states from the database that match the provided state name.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)
    cur = db.cursor()
    # Although not recommended, using string format as per the requirements.
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        fetch_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
