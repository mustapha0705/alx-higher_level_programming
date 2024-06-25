#!/usr/bin/python3
"""module that list all states with name N from database"""
import sys
import MySQLdb


if __name__ == '__main__':
    # get MySQL command
    # connect to sql server
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Execute the sql queries
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = conn.cursor()

    cur.execute(
        """
        SELECT * FROM states WHERE name LIKE BINARY 'N%'
        ORDER BY states.id ASC
        """
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
