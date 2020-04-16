import psycopg2
import sys

con = None

try:
    con = psycopg2.connect(database='postgres',user='postgres', password='postgres')
    cur = con.cursor()
    cur.execute('SELECT version()')
    ver = cur.fetchone()
    print(ver)
except psycopg2.DatabaseError as e:
    print('Error %s' % e)
    sys.exit(1)
finally:
    if con:
        con.close()