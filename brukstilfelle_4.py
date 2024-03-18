import datetime
import sqlite3

con = sqlite3.connect("TeaterDatabase.db")
cursor = con.cursor()

def checkPerformancesOnDate(date):
    cursor.execute(
        """SELECT """
    )
    return cursor.fetchall()