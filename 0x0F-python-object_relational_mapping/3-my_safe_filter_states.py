#!/usr/bin/python3
"""Module that lists all states with a name from the database."""
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python script.py <mysql_username> <mysql_password> "
              "<database_name> <state_name>")
        sys.exit(1)

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
        "SELECT * FROM states WHERE name = %s "
        "ORDER BY states.id ASC"
    )
    cur.execute(query, (state,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
