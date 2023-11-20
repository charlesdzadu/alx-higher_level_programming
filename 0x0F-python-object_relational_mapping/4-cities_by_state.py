#!/usr/bin/python3

import MySQLdb
from sys import argv

"""
lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":

    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset="utf8")
    curs = con.cursor()
    curs.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC""")
    query_rows = curs.fetchall()
    for row in query_rows:
        print(row)
    curs.close()
    con.close()
