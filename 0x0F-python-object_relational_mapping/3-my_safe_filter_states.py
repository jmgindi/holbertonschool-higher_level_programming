#!/usr/bin/env/python3
""" This script selects all states from the database hbtn_0e_0_usa
based on user input, protected from injects
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name = {}
                ORDER BY states.id ASC""", (argv[4],))

    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
