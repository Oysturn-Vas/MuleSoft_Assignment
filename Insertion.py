import sqlite3    #Inbuilt SQLite library in python

conn = sqlite3.connect('movies.db')   #Finding Database in this Folder, Else creating one.

#Create a cursor
c = conn.cursor()

#Inserting into the Movies Table
c.execute("INSERT INTO MOVIES (MOVIE_NAME,LEAD_ACTOR,LEAD_ACTRESS,YEAR_OF_RELEASE,DIRECTOR_NAME) VALUES ('Spider-Man: No Way Home','Tom Holland','Zendaya','2021-12-13','Jon Watts')")
c.execute("INSERT INTO MOVIES (MOVIE_NAME,LEAD_ACTOR,LEAD_ACTRESS,YEAR_OF_RELEASE,DIRECTOR_NAME) VALUES ('Demon Slayer : Mugen Train','Natsuki Hanae','Akari Kitō','2020-10-16','Haruo Sotozaki')")
c.execute("INSERT INTO MOVIES (MOVIE_NAME,LEAD_ACTOR,LEAD_ACTRESS,YEAR_OF_RELEASE,DIRECTOR_NAME) VALUES ('Django Unchained','Jamie Foxx','Kerry Washington','2012-12-25','Quentin Tarantino')")
c.execute("INSERT INTO MOVIES (MOVIE_NAME,LEAD_ACTOR,LEAD_ACTRESS,YEAR_OF_RELEASE,DIRECTOR_NAME) VALUES ('John Wick','Keanu Reeves','Bridget Moynahan','2014-10-16','Chad Stahelski')")


conn.commit()

#Closing the Connection
conn.close()