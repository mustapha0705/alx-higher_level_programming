#!/usr/bin/python3
"""scrpit that list all states from hbtn_0e_0_usa"""
import MySQLdb
import sys


def list_states(username, password, database):
    """lists all states from the database hbtn_0e_0_usa.
    Ags:
    username: mysql username
    password: mysql password
    database: mysql database
    """
    # Connect to the MySQL server
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = conn.cursor()

    # Execute the SQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the query result
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the database connection
    cursor.close()
    conn.close()


# Example usage
if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
