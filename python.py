import sqlite3

con = sqlite3.connect("TeaterDatabase.db")

cursor = con.cursor()

con.close()