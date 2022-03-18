import sqlite3    #Inbuilt SQLite library in python

conn = sqlite3.connect('movies.db')   #Finding Database in this Folder, Else creating one.

#Create a cursor
c = conn.cursor()

#Create a table
c.execute("""CREATE TABLE IF NOT EXISTS MOVIES(
                 ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 MOVIE_NAME TEXT NOT NULL,
                 LEAD_ACTOR TEXT,
                 LEAD_ACTRESS TEXT,
                 YEAR_OF_RELEASE TEXT NOT NULL,
                 DIRECTOR_NAME TEXT NOT NULL);
""")

conn.commit()

#Closing the Connection
conn.close()