#!/usr/bin/python3
"""
Module that lists all states with a name
starting with N from the database.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    # Get MySQL command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    # Connect to the SQL server
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = conn.cursor()

    # Execute the SQL query
    query = (
        "SELECT * FROM states WHERE name='{}' "
        "ORDER BY states.id ASC".format(state)
    )
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
