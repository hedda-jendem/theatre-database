import sqlite3

# con = sqlite3.connect("TeaterDatabase.db")

# cursor = con.cursor()

# con.close()



def execute_sql_file(filename):
    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()

    with open(filename, 'r') as f:
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

#Leser fra SQL filen vår og lager databasen
execute_sql_file('Teater.sql')