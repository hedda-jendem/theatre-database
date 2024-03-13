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
con = sqlite3.connect("TeaterDatabase.db")
cursor = con.cursor()

with open('DatabaseValues.sql', 'r') as f:
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
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,1,'Parkett',1))
#TODO SKAL VI HA MED ØVRE OG NEDRE????  


#Gamlescenen galleri 
for i in range(1, 34):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,1,'Galleri',2))

for i in range(1, 19):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,2,'Galleri',2))

for i in range(1, 18):
    cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (i,3,'Galleri',2))

#Gample scene parkett

# Antallet stoler per rad er indikert i raden under
stoler_rad = [18, 16, 17, 18, 18, 17, 18, 17, 17, 14]
stol_nummer = 1  # Starter stolnummereringen for parkett
for rad in range(1, 11):  # 10 rader totalt
    for stol in range(1, stoler_rad[rad-1] + 1):
        cursor.execute('INSERT INTO Stol (Stolnummer,Radnummer,Omradenavn,SalID) VALUES (?,?,?,?)', (stol_nummer, rad, 'Parkett', 2))  
        stol_nummer += 1

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



