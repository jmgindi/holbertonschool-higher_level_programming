#!/usr/bin/python3
""" This script selects all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities JOIN states ON state_id = states.id
                ORDER BY cities.id ASC""")
    cities = cur.fetchall()
    for city in cities:
        print(city)
