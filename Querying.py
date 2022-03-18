import sqlite3    #Inbuilt SQLite library in python

conn = sqlite3.connect('movies.db')   #Finding Database in this Folder, Else creating one.

#Create a cursor
c = conn.cursor()

#Query the Database without parameters
print("---------------------------------Querying Without Parameters----------------------\n\n")
c.execute("SELECT * FROM MOVIES")

items = c.fetchall()

print("MOVIE NAME"+"\t\t\tLEAD ACTOR"+"\t\t\tLEAD ACTRESS"+"\t\t\tDATE OF RELEASE"+"\t\tDIRECTOR")
print("-----------"+"\t\t\t-----------"+"\t\t\t-----------"+"\t\t\t---------------"+"\t\t-----------")

for item in items:
    print(item[1] + "| \t\t |" + item[2] + "| \t\t |" + item[3] + "| \t\t |" + item[4] + "| \t\t |" + item[5] + "\n")


#Query the Database with parameters
print("\n\n\n---------------------------------Querying With Parameters----------------------\n\n")
c.execute("SELECT * FROM MOVIES WHERE LEAD_ACTOR = 'Tom Holland'")

items = c.fetchall()

print("MOVIE NAME"+"\t\t\tLEAD ACTOR"+"\t\t\tLEAD ACTRESS"+"\t\t\tDATE OF RELEASE"+"\t\tDIRECTOR")
print("-----------"+"\t\t\t-----------"+"\t\t\t-----------"+"\t\t\t---------------"+"\t\t-----------")

for item in items:
    print(item[1] + "| \t |" + item[2] + "| \t\t\t |" + item[3] + "| \t\t\t |" + item[4] + "| \t\t\t |" + item[5] + "\n")

conn.commit()

#Closing the Connection
conn.close()