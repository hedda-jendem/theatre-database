import sqlite3


#Setter opp database strukturen 
con = sqlite3.connect("TeaterDatabase.db")
cursor = con.cursor()

with open('TeaterTabellSetup.sql', 'r') as f:
    sqlFile = f.read()

sql_commands = sqlFile.split(';')

# Execute every command from the input file
for command in sql_commands:
    try:
        cursor.execute(command)
    except Exception as e:
        print('Command skipped: ', e)

con.commit()
con.close()


#Setter inn verdier til databasen 






