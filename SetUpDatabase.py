import sqlite3

def read_SQL(sqlFile):
    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()

    with open(sqlFile, 'r') as f:
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

read_SQL('TeaterTabellSetup.sql')
read_SQL('DatabaseValues.sql')


#Setter opp verdier for stoler 
con = sqlite3.connect("TeaterDatabase.db")
cursor = con.cursor()

#Hovedscenen parkett 
row = 1
for i in range(1,505):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,row,'Parkett',1))
    if i % 28 == 0:
        row += 1

#Sletter de stolene som ikke finnes 
cursor.execute("DELETE FROM Stol WHERE Stolnummer IN (467,468,469,470,495,496,497,498)")

#Hovedscenen galleri
for i in range(505, 525):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,1,'Galleri',1))
#TODO SKAL VI HA MED ØVRE OG NEDRE????  


#Gamlescenen galleri 
for i in range(1, 34):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,1,'Galleri',2))

for i in range(1, 19):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,2,'Galleri',2))

for i in range(1, 18):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,3,'Galleri',2))


#Gamle scenen parkett
for i in range(1, 19):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,1,'Parkett',2))

for i in range(1, 17):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,2,'Parkett',2))

for i in range(1, 18):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,3,'Parkett',2))

for i in range(1, 19):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,4,'Parkett',2))

for i in range(1, 19):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,5,'Parkett',2))

for i in range(1, 18):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,6,'Parkett',2))

for i in range(1, 19):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,7,'Parkett',2))

for i in range(1, 18):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,8,'Parkett',2))

for i in range(1, 18):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,9,'Parkett',2))

for i in range(1, 15):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,10,'Parkett',2))


#Gamlescenen balkong
for i in range(1, 29):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,1,'Balkong',2))

for i in range(1, 28):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,2,'Balkong',2))

for i in range(1, 23):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,3,'Balkong',2))

for i in range(1, 18):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,4,'Balkong',2))

con.commit()
con.close()



