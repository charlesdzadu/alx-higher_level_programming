#!/usr/bin/python3


import MySQLdb
from sys import argv

'''
Script that lists all states
'''
if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    curs = con.cursor()
    curs.execute(
        "SELECT * FROM states WHERE name LIKE"
        " '{:s}' ORDER BY id ASC".format(argv[4]))
    db = curs.fetchall()
    for i in db:
        if i[1] == argv[4]:
            print(i)
