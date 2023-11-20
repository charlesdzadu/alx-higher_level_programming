#!/usr/bin/python3


import MySQLdb
from sys import argv

'''
lists all states with starting name with N
'''
if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    curs = con.cursor()
    curs.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%'ORDER BY id ASC")
    db = curs.fetchall()
    for i in db:
        print(i)
