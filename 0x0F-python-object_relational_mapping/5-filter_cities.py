#!/usr/bin/python3
"""
A script that takes the name of a state as an argument and lists all cities of
that state from the database 'hbtn_0e_4_usa', ensuring the query is safe from
SQL injection.
"""

import MySQLdb
import sys


def list_cities(username, password, dbname, state_name):
    """
    Fetches and prints all cities for a given state in a safe manner to prevent
    SQL injection.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)
    cur = db.cursor()
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    # Collecting city names and joining them with a comma
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
