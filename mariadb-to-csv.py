# requirement: mysql-connector

import mysql.connector as mariadb
import sys
import csv

QUERY='SELECT * FROM table.name;'
mariadb_connection = mariadb.connect(user='user.name', password='user.password', database='database.name')

cur = mariadb_connection.cursor()
cur.execute(QUERY)
result=cur.fetchall()

# File mode, write and binary
c = csv.writer(open('dump-file-name.csv', 'wb'))
for x in result:
    c.writerow(x)
