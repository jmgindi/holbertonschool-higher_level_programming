#!/usr/bin/python3
""" This script selects all cities of a specific state
from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities
                JOIN states ON state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC""", (argv[4],))
    cities = cur.fetchall()
    print(", ".join([city_name for city in cities for city_name in city]))

    cur.close()
    db.close()
