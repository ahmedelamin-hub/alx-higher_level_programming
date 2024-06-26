#!/usr/bin/python3
"""
A script that lists all cities from the database 'hbtn_0e_4_usa'.
Results are sorted in ascending order by cities.id.
"""

import MySQLdb
import sys


def list_cities(username, password, dbname):
    """
    Connects to the MySQL database and retrieves all cities, sorted by city ID.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)
    cur = db.cursor()
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
